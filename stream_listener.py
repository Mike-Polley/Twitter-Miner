from tweepy.streaming import StreamListener
import sentiment_analyser
from tweet_cleaner import tweet_cleaner
import time
import datetime
from settings import c
from dateutil import parser

# provides a custom twitter stream listener change the on_status function fields
# list to add or remove fields

class CustomStreamListener(StreamListener):

    def __init__(self,api=None):
        self.api = api

    def on_status(self,status):
        if not '@RT' in status.text:
            tweet = tweet_cleaner(status.text)
            username = tweet_cleaner(status.user.screen_name)
            date = parser.parse(str(status.created_at).encode('utf-8'))
            geo = status.geo
            sent_comp = sentiment_analyser.raw_comp(tweet)
            sent_norm = sentiment_analyser.overall_sent(tweet)
            likes = status.favorite_count
            # retweets = status.retweet_count
            params = [tweet,username,date,geo,sent_comp,sent_norm,likes]
            c.execute('Insert into dbo.Tweets values (?,?,?,?,?,?,?)',params)
            c.commit()

    def on_error(self,status_code):
        if status_code == 420:
            print('Error code 420 at: '+str(datetime.datetime.now()))
            time.sleep(900)
        return False
