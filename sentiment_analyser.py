from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# These functions analyse the sentiment using Vader sentiment analyzer of a given text string
# they provide both a string value as well as the raw integer value

# compound sentiment
def raw_comp(text):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)
    sentiment = score['compound']
    return sentiment

# negative sentiment
def raw_neg(text):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)
    sentiment = score['neg']
    return sentiment

# positive sentiment
def raw_pos(text):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)
    sentiment = score['pos']
    return sentiment

# neutral sentiment
def raw_neu(text):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)
    sentiment = score['neu']
    return sentiment

# overall sentiment as a string
def overall_sent(text):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)
    sentiment = score['compound']
    if sentiment >= 0.05:
        return 'Positive'
    elif (sentiment > -0.05) and (sentiment < 0.05):
        return 'Neutral'
    else:
        return 'Negative'
