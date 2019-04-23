from tweepy import Stream,OAuthHandler
from tweepy.streaming import StreamListener
import stream_listener
from settings import consumer_key, consumer_secret,access_token,access_token_secret, tracked_tags

# sets up the authorisation required for twitter miner sets stream values and runs
# function

def twitter_miner():
    auth = OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    listener = stream_listener.CustomStreamListener()
    stream = Stream(auth,listener,tweet_mode=['extended'])
    stream = stream.filter(track=tracked_tags,languages=["en"],is_async='True')
    return stream

twitter_miner()
