from flask import Flask, jsonify, request
from data_collection import collect_tweets
from sentiment_analysis import analyze_sentiment
from visualization import plot_data

app = Flask(__name__)

@app.route('/collect', methods=['GET'])
def collect_and_analyze():
    keyword = request.args.get('keyword', default='Python', type=str)
    tweets = collect_tweets(keyword)
    sentiments = [analyze_sentiment(tweet) for tweet in tweets]
    return jsonify(sentiments)

@app.route('/visualize', methods=['GET'])
def visualize():
    # Dummy data for visualization
    data = [1, 2, 3, 4, 5]
    plot_data(data)
    return "Data plotted. Check your plot viewer."

if __name__ == '__main__':
    app.run(debug=True)
