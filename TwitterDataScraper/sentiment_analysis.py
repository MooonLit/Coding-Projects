from textblob import TextBlob

def analyze_sentiment(tweet):
    analysis = TextBlob(tweet)
    return analysis.sentiment
