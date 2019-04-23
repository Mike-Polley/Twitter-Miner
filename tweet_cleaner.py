from unicode import unicodetoascii as uniasci
from re import sub

# function cleans twitter text to remove web addresses, unicode characters and other
# non asci characters

def tweet_cleaner(tweet):
    tweet = tweet.encode('utf-8')
    tweet = str(tweet)
    tweet = uniasci(tweet)
    tweet = sub(r'RT @[\w]*:','',tweet)
    tweet = sub(r'RT @[\w]*:','',tweet)
    tweet = sub(r"b'",'',tweet)
    tweet = sub(r'b"','',tweet)
    tweet = sub(r'@[\w]*','',tweet)
    tweet = sub(r'\w\w\d','',tweet)
    tweet = sub(r'\d\w\w','',tweet)
    tweet = sub(r'\\...','',tweet)
    tweet = sub(r'https?://[A-Za-z0-9./]*','',tweet)
    return tweet
