# Repup.co-Assignment

The task was to scrape news sources for the last five days (News Websites, blogs, etc.) and construct the cumulative sentiment analysis of articles with respect to cities. 

To solve this task, first I scrapped thr citywise news headlines
https://blogs.timesofindia.indiatimes.com/city.
Scrapped is done for following cities  Delhi, Mumbai, Hyderabad and Chennai.
Code for scrapping is written in scrap_n_save.
The scrapped data is saved in data.csv file.

As the scrapped data doesn't have any labels and there was no website from which I could extract news with labels given already. So, labelling task has to be done manually.
The labelling of the news is done as follows: 
-1 for news with negative sentiment.
0 for news with neutral sentiment.
and 1 for news with positive sentiment.

For sentiment analysis, first the dataset is splitted into training and test dataset.

Then, Converted the texts into feature vectors using count vectorizer and tf-idf vectorizer
 and used multinomial naive bayes classifier for training and testing the data.
Submission.csv file gives predicted sentiment of the cities.
