# Tweet_Analyser

The CET300 project which this document scopes is “Analysing and Determining the Evolution of Hate Speech”. This project is a client-based project which has been commissioned by Sadar Jaf from the Faculty of Computer Science of the University of Sunderland

Due to the nature of the proposed system the interface development was one consideration which had to be accounted for. Upon clients request the application was to be driven by the systems functions as opposed to a resource heavy graphical interface. Recommendations made to exclude a GUI were made by the client and followed through. However, one of the most important non-functional requirements gathered during the requirement elicitation was to improve performance of the application. This was achieved by ensuring the application implemented a command interface with the idea of user interactivity and usability in mind. As stated by Hayes and Szekely, (1983) command interfaces for applications fail to deliver prompt error correction or in-line help towards users, which leads to a perception of unfriendly or inaccessible interfaces, which can further lead to frustrations within the users. To remedy this the focus of the command interface development turned to providing users with prompt instructions and error corrections upon incorrect inputs. This allowed for the interface to funnel users to the end goal of the system allowing for a smooth and seamless transition between functions. 
  
Fig 1. Code example of system processing user input.
Fig 1. shows a code example displaying how the system will prompt the user for input and how this input will be processed  The few methods used here to ensure that the system is accessible and user friendly are the use of the .strip() function in conjunction with the .lower() method. The .strip() function ignores any white space surrounding the user input be it before or after any text within the string. It then returns the same string to the system without the empty spaces. Once the string has been returned the system then processes the returned string once more using the .lower() function which returns the string without white spaces as a lowercase string. This means that any variations on the requested input by the user will be compared in the most uniform of ways to mitigate any misunderstanding by the user in turn reducing the chances of simple errors which could be in place if these functions were ignored. Below are examples of the system processing user input using these methods.

Fig 2. showing System accepting lowercase input with white space.



Fig 3. showing System accepting uppercase input with white space.

Fig 4. Code example of In line help.

Fig 4. Is an example of how the system will handle guiding the user and being as transparent as possible with the philosophy of providing the user with as much inline help and information as possible. In this example the system will be storing a predefined string which has the sole purpose of being printed after the data save function has been passed or completed. Upon successful completion of the user saving analytical data as a csv file the system will primitively update the string to display the correct string showing the user that the information has been saved. If the function is ignored, then the system can print the predefined string and inform the user that the data has not been saved. This is vital for the user experience as it will ensure there is no miscommunication between system and end user which in turn will improve the users overall experience and in turn make the system much more accessible for the end user. This will also help build a sense of repour and allow for experienced users to realise when the system has not completed the tasks if a mistake is made upon use.

Fig 5. Showing in line help being displayed by the system.

5.1.1.	 Data visualisation Interface

One of the most important aspects within the system to focus on during the development phase was the interface for the data visualisation. As the intention for the interface throughout the design was to ensure an effective and easy to run system which was accessible through a low entry point in terms of computer specifications. This was done for the command interface design but was a much more important consideration for the data visualisation. Due to the design documentation along with a firm understanding of the application specifications gathered during this project, the development of this interface was smoothly and seamlessly worked on after design documentation and planning documentation was completed in conjunction with the command interface development. Throughout the planning and design documentation for the interface design I.E. the design interface wireframes it was decided the data visualisation would be handled by Matplotlib. Matplotlib is a python library which allows for plotting of data in various forms and factors. For this application a line graph which displayed metrics over time for a tweet was decided. This method would meet the functional requirements set out by the client. Matplotlib offers a simple interface which allows for a low usage of resources; however, the interface is clean and minimalistic which allows for an easy to read metrics and user-friendly experience. The interface can be manipulated to allow for expression of details according to the specificness of the application or system. The development of the interface for data visualisation was seamlessly worked on in conjunction with the system design as the two are heavily reliant on one another. The interface was straightforward to develop, however there were important things to consider. For example, the user is to be able to visualise data based on likes over time, retweets over time and there should be the inclusion of a visualisation plot which shows both side by side.
 
Fig 6. Code example of how Single metric plot interfaces were designed.

 
Fig 7. Data visualisation interface running.

Fig 6. And Fig 7. Show the both  the code and the final result whilst the system is running, these examples show how the systems interface is set up and how the interface is displayed, however they are only based on the single metric system which has a lack of subplots, this makes the interface much more simplistic and easier to develop, on the other hand without the use of a sub plot displaying both metrics in one plot would be impossible as matplotlib uses subplots to separate data allowing for the use of multiple plotting. A work around for this issue was to include subplots only when the user selects the option of displaying both metrics. This would save resources and make the application much more proficient in terms of processing. The interface itself borrows data from the analytical field and the system development to allow for relevant information to contextualise the interface, for example the ID field borrows from the tweet ID of each individual tweet to separate the lines based on a colour value. The dates field and likes field in a similar manner borrow from the corresponding fields from within the tweets pulled through twitter, however, the Titles and labelling were manually added to make the interface make much cleaner to read which would aid users when analysing data and making quick judgement calls.
 
Fig 8. Code example of creating subplots for each metric measured in the system.

 
Fig 9. Running Example of Subplots displaying both measured metrics.

Fig 8. And Fig 9. are primary examples of how subplots can be developed to showcase two different plots showcasing separate data. These examples from the system show how powerful subplots can be for analysis as it is possible to do accurate comparison analysis when the two graphs are displayed side by side in a single plot. These are very similar to the single metric system used; however, they are instantiated through ax variables which have a position passed into their axis which dictates where these plots will be displayed individually. Once the plots have been set as variables and each attribute is selected, the titles and labels can be added to each of them before telling the system to show the plot. This method is slightly more complex than the single metric system used for the other metrics, however the complexity in this case does not affect the performance in a negative way which is important when considering that having a lightweight interface will increase overall performance for the system.
5.2.	System Development

The process in which development took place was split into eight different phases. Each of these were worked on independently and in a sequence, which would allow for future functions to be moulded based on previous phases and vice versa. The first phase was to develop a form of Twitter streaming which granted access to the Twitter API to the application. This was also used to help develop an understanding of how twitter data was parsed and was achieved by using the Tweepy library using Python. The next step was to refine data retrieval using historical data, which was possible using Tweepy’s API cursor, this step allowed for data to be pulled through based on search terms and popularity for the purpose of data manipulation. Once apt data is retrieved the next step in development was to process data, which was possible using Pandas and numpy to allow for additional computational power to process tweets and manipulate them based on specific attributes to be further analysed. Upon processing, the data was analysed and sent through a sentiment analysis function to give an accurate reading using collated and pretrained data using the Textblob library in Python. Once sentiment analysis has been completed the applied and Tweets have been analysed the next phase of development was to create method of saving analytical data which was also possible using the Pandas library, Pandas is also used to prepare data for visualisation which then leads to the final step of sending the information through a plot to be displayed using Matplotlib.



5.2.1.	Twitter Streaming

During the system development one of the first functions added to the system was the ability to stream tweets. This was done for a multitude of reasons, the first being to gain familiarity with how the Tweepy library interacts with the twitter api. The second main reason this was done was to gain an understanding which information is received from twitter. As the agile methodology was being used, this function was in development in conjunction with, planning, research and design, due to this it was important to understand which information a tweet would contain and how that information would display to the end user. As the end goal of the system is to display tweets and analyse them based on the information provided, processing and pre-processing would need to be conducted, therefore understanding which information is passed through the api is important to assess which data is relevant and irrelevant. In addition, incorporating this function first not only gave access to the api, it provided an introduction into the systems which will be handled and dealt with during the course of the project. Incorporating this function first would allow the introduction of systems which would be used further down the development line such as the TwitterClient class and the Twitter Authenticator class. The TwitterClient class was in place to retrieve information from the twitter api such as tweets from timelines or users’ followers. The Authenticator was in place to access the twitter credentials such as consumer keys and api keys saved within a separate script in the same directory.

Fig 10. TwitterClient Class.

 
Fig 11. Twitter Authenticator Class.
The incorporation of these features was important for the system as a whole, these functions were in place in part due to the twitter streaming system as it relied on these systems. However, they were used as a base foundation which allowed for building blocks to be placed upon them such as the ability to pull historical data from Twitter. The two specific functions used to stream tweets were the TwitterStreamer class and the TwitterListener class which would print the processed live tweets. Below are examples showing the code from the system used.






Fig 12. Twitter Streamer:









Fig 13. TwitterListener.

The end result of this function was allowing for a strong foundation to be built in terms of authentication and a function to access historical data which would be important when it came to the analysis of actual tweets going forward for the system to meet the client’s requirements. Along with an understanding of how overwhelming tweet information can be if not processed correctly. Fig 14. is an example of how each tweet is parsed and which information it contains.
 
Fig 14. Twitter Streamer Running. 

5.2.2.	Retrieving Twitter Historical Data

Due to the addition of the twitter streamer function and the addition of the Twitter Client the ability to retrieve historical data was something considered early on in development due to requirement gathering and system design documentation. Historical data in terms of twitter is any tweet that has been publicly posted and is available through the API, this can be considered as any tweet available on the website at any given moment. With the Twitter Client the use of the cursor can be used through the api to pull any historical data based on queries and other factors such as popularity or time of posting. The cursor can be used for specific users to pull all tweets within the associated timeline. However, for the purpose of this project the idea was to allow for users to use the cursor api and a user inserted query to dynamically insert tweets to a data frame for analysis. The first hurdle to overcome was already dealt with as the TwitterClient function was added at beforehand which would allow access to tweets and return them into an array. However, the next step would be to allow for using the Twitter client to retrieve the api, the api would then be used to search for tweets using the attributes inserted. In this case the attributes are as follow: q stands for search query; count stands for the number of tweets to search for and the result_type is used to pull in popular tweets. This can be seen within Fig 15.
 
Fig 15. Pulling historical users using api cursor.

To receive user input and allow for dynamically input data the variable term is used within the system which will prompt the user to input a search term, this will then prompt the user to enter a number to load into the system which will allow for a dynamically inserted count. For the variable term the strip method was used to allow for the removal of white spaces, however the .lower() function was excluded as twitter search terms or screen names often contain uppercase characters. This is a more prominent issue if the api cursor is used to search for screen names or users as opposed to queries. An explanation of how errors are handled is explained within the command interface section above. This function was seamlessly integrated into the system due to asynchronous work done through the early sprints of development and design along with planning. Having a strong understanding of the final application and the steps required to take to develop such a system allowed for an efficient workflow and functionality to be added in a sequential but segmented approach.






Fig 16. Code running displaying the use of dynamically inserted search terms
5.2.3.	Processing and Analysing Tweets

Once the system has been given a dataset. In this case a dynamically inserted database based off of tweets the user has loaded, the next important step is to process the tweets and apply analysis. During the development of the system a function named Tweet Analyser was developed. This function’s primary focus was to process tweets and include relevant information. The function included methods within which would allow for manipulation of information before saving it into a Pandas data frame to be sent to finalised analysis and visualisation. This was one of the most essential systems involved in the final prototype as it would allow for manipulation of data to be made along with visualisation. The main function included within the Tweet Analyser was the method which would send tweets to the data frame. This works by creating a new data frame which uses relevant tweet information as columns. These can later be manipulated further once the data has been inserted into the data frame based on conditions or other such factors. 
 
Fig 17. Processing relevant information using Pandas Data frame.

Fig 17. Show cases how this is done, the application will create a new data frame which will use the text of the tweets as a base column for tweets. Once done it is possible to add columns into the data frame using numpy arrays which will cycle through each tweet within the tweets array which is contained within the TwitterClient function. Some columns may seem redundant such as the influencer column which seems to be the same as the follower’s column, however this is implemented to be manipulated further down in the code. Fig 18. Shows how this is possible.
 
Fig 18. Conditional Replacement to manipulate data.

In Fig 18. The .loc method is used on a data frame to replace information in the influencer column, this is done by checking the condition of the followers column. As recommended by the client the system should detect if a Twitter user is an influencer based off of their follower count. The number suggested by the client was 10,000. These lines of code check whether or not a tweet’s user meets the condition, upon which it will replace the values within the influencer column. 
Using the follower column to make the comparison as opposed to the influencer column set up within the Tweet Analyser function is essential, if one were to try applying these conditions from the same column being edited the system would throw an error due to mixed data types. This is an issue which was problematic during development, which was remedied by using the follower’s column as the conditional.
5.2.4.	Sentiment Analysis

One of the most important functions to include during the development of the system was the sentiment analysis. Sentiment analysis was included within the functional requirements made by the client and was included within the design and analysis of the system. Chapter 2 included an in depth study on the classification methods which could be applied to allow for an accurate analysis of sentiment in terms of Twitter. The final system is to provide the user with analytical statistics which are to be used to make deductions or further external analysis. Due to this including a form of sentiment analysis is essential as it will provide extra information to the user. Python offers many libraries which can be used to make workloads more efficient, when designing and planning the system the Textblob library which is part of the Sklearn family was recommended. This library was recommended as it offers a trained classifier which has forks in the world of analysing twitter making it a great alternative as it has been used in the field before. The use of Textblob was essential as the time constraints would not allow for a fully developed classifier for the application, this was important to keep in mind whilst developing as the systems main functionality was to be the analysis of tweets and the data visualisation, this was stressed by the client as sentiment analysis was a secondary functionality to considered once the main functionality was added. This function however was prioritised once the processing of data was completed. Fig 17. shows each column which is associated with a tweet. However, the beauty of pandas and data frames is the power of data manipulation. As seen with the influencer column. It is possible to replace values within columns. To take this further the sentiment analysis column can be added holey after each other column to allow for processing of tweets and associating sentiment scores. 

Fig 19. Cleaning tweets for sentiment analysis.

Fig 19. shows one of the most important steps which must be taken before applying the sentiment function to a tweet. This precaution must be taken to prevent the classifier getting confused, the classification. In this case, TextBlob was trained without these character present, therefore introducing these elements in the released classification system would lead to unpredictable results.







Fig 20. Applying Sentiment and Returning Value.
Once the tweet has been cleaned for the purpose of sentiment analysis the analyze_sentiment function is applied to the tweet. The polarity is checked by the system and a value is returned, if the value is above 0 the sentiment will be returned as 1 which means that the system classifies the Tweet as positive. If the system detects that the polarity of the tweet is 0 then it will return a 0 value which in turn means the system identifies the tweet as neutral, and in any other cases, the system will return the value -1 which suggests a negative value. This is then returned as a string with the corresponding meanings to allow for an easier to understand output for the user. 
Fig 21. Applying Sentiment analysis to each Tweet.

Once the function has been written the final step to apply the sentiment analysis to each tweet being processed within the data frame is to create a column using a numpy array and allow it to create a “for each” statement which uses the sentiment analysis function and passes through each tweet as the parameter. This will allow for each of the individual tweets within the column to produce its own individual sentiment score. Which allows for further examination and analysis to be conducted on an individual tweet basis by the user of the system which in turn achieves the functional requirement set out by the client. 
Fig 22. Showcase of final Sentiment output within the System.

5.2.5.	Saving Analytical Data

One of the functional requirements gathered during the analysis phase of this project was the ability to save analytical data. The client recommended allowing for data to be saved in the form of a CSV, this was to be a simple function which would allow for the user to save the data as a CSV file to then further analyse the data. Due to the fact Pandas was used for the development of this application, this was possible with a few simple lines of code. The application first provides the user with a prompt querying if the user wishes to save the data frame as a CSV file, upon answering yes, the system will save the data as a CSV file using the search term as a file name. If the user wishes not to save the data, the application will move to the next step without saving the data. 

Fig 23. Code used to save data as CSV.

The string which is stored with the response for a user not saving information as a CSV is created before the system prompts the user to save the file, this is to allow for a dynamic response based off of the users interaction, if the user responds with a positive response, in this case, a “y” then the data frame will be saved as a CSV file using the variable as a file name, the value of the string will be changed to state the data has been saved, and the string will be printed. However, if the user provides a negative response the application will simply print the string which was created at the beginning of the function, which states the data will not be saved.










Fig 24. Saving Data through interface.






Fig 25. File Saved to Directory of Application.









Fig 26. Showcase of Saved CSV.

Fig. 24, Fig 25. and Fig 26. showcase the functionality of the saving data system and how effective it can run. The importance of creating a user-friendly system which incorporates all aspects of the design philosophy discussed in the previous chapter are all primarily displayed within this function. The added error handling, mitigation of incorrect inputs and the use of a funnelling system which easily allow for users to save data, these all allow for the system to meet the requirements set out by the client, both functionally to save data and non-functionally to provide a seamless experience.
5.2.6.	Preparing data for visualisation

Data visualisation was one of the most important functional requirements as the systems main goal was to display analytical data over a course of time. Many considerations were made and followed during the development, design and analysis phases. Due to the agile methodology in place, there were many attempts to visualise data, however all resulted in failure due to the way in which the twitter api handles and sends data. This made the visualisation almost impossible as the statistics would align only to creation date and final value of likes or retweets at the time of the information being pulled. Due to this intensive research and trial and error methods were used to arrive at a method in which it would allow for visualisation over time. The final prototype system incorporated a function which would prepare data for visualisation. When twitter information is received by the system and processed within the data frame the data is displayed as shown in Figure 27.






Fig 27. How Tweet Data is processed.

With the information being shown in columns regardless of the data provided by twitter, in this case a lack thereof information based on likes or retweets per day for each tweet. Visualisation would be impossible without a manner of switching the columns and rows. This was overcome with the function included in pandas known as Pivot. The pivot function allows for the table to be manipulated based on specific fields. Once the data has been pivoted the ability to visualise the data can be simplified into a few simple lines of code. This however does cause issues in itself as it essentially creates a new data frame with the pivoted data. This means that each of the metrics will need to create a perseverate data frame based off of user input. 
Figure 28. Code used to pivot Data.

The use of this code allows for the manipulation of data. The attribute values refer to the values within the columns inside the data frame. The index refers to the Rows included within the data frame and the columns refers to the columns included within the data frame. In the example of Fig 28. The code is used for the pivoting of retweets. This means that the retweets are used as the values, the dates are used as the index and the columns are based off of the IDs. The system must remove all NaN values to allow for measurements over a course of time. This is done by including the attribution “fill_values = 0”

5.2.7.	Visualising Data

The visualisation of Data is the final step within the funnel of the system. With this being the end goal of the system, it should be noted that this functional requirement is also one of top priority. This is essentially as noted within the design documentation the final step a user will go through before the system loops to allow for a new set of data to be input. The visualisation of data was developed alongside the development of the pivot function which would allow for the correct data to be displayed over a period of time on a line plot. The interface and functional design wireframes completed aided in both the appearance of the final visualisation of data and the functionality which was bundled alongside it. The visualisation was to be implemented for each metric, as discussed in the interface section of this chapter there were many different factors to include such as sublots and ensuring the interface was developed correctly to represent the design conducted during the course of the project, The final visualisation would simply require input of data from the data frames created in instances where data was pivoted to allow for accurate values and metric.













   Fig 29. Code showcasing how Data was visualised.

Fig 29. Showcases how the data was visualised including the methods discussed previously to prepare the data for visualisation. Once the data was pivoted for plots which required single metrics to be visualised such as the retweets plot it was possible to simply add a plot function using the matplotlib library and include labels to create a well-designed plot. 
For a more complex plot such as the final plot which included both likes and retweets in a single plot to enable comparative analysis. The use of subplots was essential, this was done by creating two plot variables and assigning a value for their axis which would allow for manipulation of the plot for each metric separately, for example applying separate labels and including separate values for each sub plot. Both of these methods were functional requirements and therefore were included within the final prototype. 
As shown in Fig 29. a while loop was used to handle errors within this function. This was done for the purpose of making the application much more user friendly and accessible, as the data visualisation is the final step within the system flow. It is important that the system does not allow for a simple error or misspelling to cause the user to restart the system or go through the previous steps once more. This is to avoid frustration and enhance the users final overall experience, and to allow for a seamless system with efficient performance. 










Fig 30. Error Handling During Data Visualisation Prompt.













Fig 31. Final Data Visualisation Single Metric.










Fig 32. Subplots used for Comparative Analysis.

5.3.	Summary

Overall the development process of the project in terms of objectivity has been a success. The system fulfils each functional requirement set out by the client and overall the system satisfies the clients final vision for the project, this includes features which were not requested by the client such as clear error handling, focused sentiment analysis or a method for the system to allow for the user to insert a new data set once the process was completed. These were included with initiative which was sparked by interest and passion for the project during the research and design phases respectively. This aided overall in creating an interface which may not be graphically intensive but provides a seamless experience with a concise goal in mind. Despite the development process of the project feeling to be a success based upon client’s requirements, and functionality included within the system the testing process will dictate the true level of success the application has. The testing will provide an accurate idea of how well the system runs, how accessible the application is and if the application can be deployed as a prototype in the analytics field. This discussion will be further ignited and concluded with evidence during the Testing and Evaluation Chapters respectively. However the development of the project thus far has been a success with the development chapter being one of the major phases conducted, it is important to realise that within the time constraints involved, there is a number of improvements which could not be made such as implementing an individually created sentiment classification system or allowing for processing and analysis of tweets as they are being streamed. These functions could be added into future considerations however with the time given for this project they are all but impossible to add. Many bugs were dealt with but most of the development time was spent learning new technologies such as Pandas and specific python libraries, along with learning the capabilities of each and how one can manipulate each aspect of specific libraries to create a seamless application, with the end process being the prototype developed for this project. 

