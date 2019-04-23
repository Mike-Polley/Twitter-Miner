"# Twitter-Miner"

This script mines all tweets for a specific hash tag using the Tweepy module using the twitter stream API.
It loads these into a SQL server using PYODBC and uses Vader Sentiment to analyse the sentiment of each tweets
ascribing this a float value as well as a string representation.

The settings.py should be used to add all relevant twitter sign in details, as well as the SQL connection string
and followed #tags.

Dependencies;
PYODBC
Vader sentiment
Tweepy
DateUtil
