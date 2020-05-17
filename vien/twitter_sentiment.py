from flask import Flask, render_template, request, redirect, url_for
from joblib import load
from twitter_api import get_related_tweets


pipeline = load("Text_Classsfier.joblib")


def result(name):
    tweets = get_related_tweets(name)
    tweets['prediction'] = pipeline.predict(tweets['tweet_text'])

    data = str(tweets.prediction.value_counts()) + '\n'

    return data + str(tweets)


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/', methods=['POST', 'GET'])
def getdata():
    if request.method == "POST":
        usr = request.form['search']
        return redirect(url_for('success', name=usr))


@app.route('/success/<name>')
def success(name):
    return "<xmp>" + str(result(name)) + "<xmp>"


if __name__ == "__main__":
    app.run(debug=True)
