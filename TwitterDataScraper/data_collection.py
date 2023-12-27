from auth import authenticate
import tweepy

def collect_tweets(keyword, max_tweets=100):
    api = authenticate()
    tweets = []
    for tweet in tweepy.Cursor(api.search, q=keyword, lang="en").items(max_tweets):
        tweets.append(tweet.text)
    return tweets
