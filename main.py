from tweepy import API 
from tweepy import Cursor
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob
import re
import twitter_credentials
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json


# # # # TWITTER CLIENT # # # #
class TwitterClient():
    def __init__(self, twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = API(self.auth)

        self.twitter_user = twitter_user

    def get_twitter_client_api(self):
        return self.twitter_client

    def get_user_timeline_tweets(self, num_tweets):
        tweets = []
        for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items(num_tweets):
            tweets.append(tweet)
        return tweets

    def get_friend_list(self, num_friends):
        friend_list = []
        for friend in Cursor(self.twitter_client.friends, id=self.twitter_user).items(num_friends):
            friend_list.append(friend)
        return friend_list

    def get_home_timeline_tweets(self, num_tweets):
        home_timeline_tweets = []
        for tweet in Cursor(self.twitter_client.home_timeline, id=self.twitter_user).items(num_tweets):
            home_timeline_tweets.append(tweet)
        return home_timeline_tweets


# # # # TWITTER AUTHENTICATER # # # #
class TwitterAuthenticator():

    def authenticate_twitter_app(self):
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        return auth

# # # # TWITTER STREAMER # # # #
class TwitterStreamer():
    """
    Class for streaming and processing live tweets.
    """
    def __init__(self):
        self.twitter_autenticator = TwitterAuthenticator()    

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # This handles Twitter authetification and the connection to Twitter Streaming API
        listener = TwitterListener(fetched_tweets_filename)
        auth = self.twitter_autenticator.authenticate_twitter_app() 
        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords: 
        stream.filter(track=hash_tag_list)


# # # # TWITTER STREAM LISTENER # # # #
class TwitterListener(StreamListener):
    """
    This is a basic listener that just prints received tweets to stdout.
    """
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True
          
    def on_error(self, status):
        if status == 420:
            # Returning False on_data method in case rate limit occurs.
            return False
        print(status)


class TweetAnalyzer():
    """
    Functionality for analyzing and categorizing content from tweets.
    """
    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def analyze_sentiment(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))
        
        if analysis.sentiment.polarity > 0:
            return "Positive"
        elif analysis.sentiment.polarity == 0:
            return "Neutral"
        else:
            return "Negative"
    
        
    def tweets_to_data_frame(self, tweets):
        df = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])

        df['id'] = np.array([tweet.id for tweet in tweets])
        df['len'] = np.array([len(tweet.text) for tweet in tweets])
        df['date'] = np.array([tweet.created_at for tweet in tweets])
        df['source'] = np.array([tweet.source for tweet in tweets])
        df['likes'] = np.array([tweet.favorite_count for tweet in tweets])
        df['retweets'] = np.array([tweet.retweet_count for tweet in tweets])
        df['followers'] = np.array([tweet.user.followers_count for tweet in tweets])
        df['verified'] = np.array([tweet.user.verified for tweet in tweets])
        df['user'] = np.array([tweet.user.screen_name for tweet in tweets])
        df['Influencer'] = np.array([tweet.user.followers_count for tweet in tweets])
        return df

 
if __name__ == '__main__':

    twitter_client = TwitterClient()
    tweet_analyzer = TweetAnalyzer()
    continueint = 1
    while continueint < 2:
        api = twitter_client.get_twitter_client_api()
        term = input("Enter Search term for Twitter ")
        intresult = None
        while intresult is None:
            countsize = input("Please enter number of tweets to load ")
            try: intresult = int(countsize)
            except ValueError: pass
        tweets = api.search(q=term.strip(), count=countsize, result_type='popular')
        
            

        df = tweet_analyzer.tweets_to_data_frame(tweets)
        df['sentiment'] = np.array([tweet_analyzer.analyze_sentiment(tweet) for tweet in df['Tweets']])
        df.loc[df.followers > 10000, 'Influencer'] = "yes"
        df.loc[df.followers < 10000, 'Influencer'] = "no"
        
        print(df)
        string = "Data will not be saved"
        save = input("would you like to save these results as a csv? y/n ")
        if save.strip().lower() == 'y':
            df.to_csv(term + '.csv')
            string = "Data has been saved to a csv"
        print(string)
            
        #print(dir(tweets[0]))
        #print(tweets[0].retweet_count)
        i = 1
        while i < 2:
        
            response = input("which metric would you like to analyse? L for likes, R for Retweets or B for both ")
            if response.strip().lower() == "r":
            
                df2 = pd.pivot_table(df, values='retweets', index=['date'],
                                columns=['id'], aggfunc=np.sum, fill_value=0)
                df2.plot(marker='o', lw=4, markersize=10, markerfacecolor='black')
                plt.ylabel('Retweets', fontsize=15, weight='bold')
                plt.xlabel('Dates', fontsize=15, weight='bold')
                plt.title('Retweets Over Time', fontsize=20, weight='bold')
                plt.show()
                i += 1
            if response.strip().lower() == "l":
                df2 = pd.pivot_table(df, values='likes', index=['date'],
                                columns=['id'], aggfunc=np.sum, fill_value=0)
                df2.plot(marker='o', lw=4, markersize=10, markerfacecolor='black')
                plt.ylabel('Likes', fontsize=15, weight='bold')
                plt.xlabel('Dates', fontsize=15, weight='bold')
                plt.title('Likes Over Time', fontsize=20, weight='bold')
                plt.show()
                i += 1
            if response.strip().lower() == "b":
                df2 = pd.pivot_table(df, values='retweets', index=['date'],
                                columns=['id'], aggfunc=np.sum, fill_value=0)
                df3 = pd.pivot_table(df, values='likes', index=['date'],
                                columns=['id'], aggfunc=np.sum, fill_value=0) 
                fig, axes = plt.subplots(1, 2)
                #df2.plot(marker='o', lw=4, markersize=10, markerfacecolor='black')
                #df3.plot(marker='o', lw=4, markersize=10, markerfacecolor='black')
                
                ax = df2.plot(ax=axes[0], marker='o', lw=4, markersize=10, markerfacecolor='black')
                ax2 = df3.plot(ax=axes[1], marker='o', lw=4, markersize=10, markerfacecolor='black')
                ax.set_xlabel('Date', fontsize=15, weight='bold')
                ax.set_ylabel('Retweets', fontsize=15, weight='bold')
                ax.set_title('Retweets Over Time', fontsize=20, weight='bold')

                ax2.set_xlabel('Date', fontsize=15, weight='bold')
                ax2.set_ylabel('Likes', fontsize=15, weight='bold')
                ax2.set_title('Likes Over Time', fontsize=20, weight='bold')
                plt.show()
                i += 1
                exitinput = input("would you like to continue? y/n")
                if exitinput.strip().lower() == "n":
                    print("Exiting application")
                    continueint += 1
                elif exitinput.strip().lower() == "y":
                    print("Continuing")
                    continue 
            else:
                print("Incorrect input please try again")
        
        
            





    # Time series
    



