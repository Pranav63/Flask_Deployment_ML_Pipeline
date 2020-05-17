import tweepy
import pandas as pd
import time

pd.set_option('display.max_colwidth', 1000)

api_key = "2aBkhROslozQWBzap6zFxYFIe"
api_secret_key = "bLts6bAzUn9VNWRPCoGMjowugcEkAvMHmQjoTn6U3TBKxCbBv5"
access_token = "895640034488991744-OAqXX0PJsUvd28twnCtRv3RGW9acGJ8"
access_token_secret = "dAMrthVP5r2jv58kUHrYOmo7tLgnyljQZYS8XCTTAhnvY"

authentication = tweepy.OAuthHandler(api_key, api_secret_key)

authentication.set_access_token(access_token, access_token_secret)

# call api

api = tweepy.API(authentication, wait_on_rate_limit=True)


def get_related_tweets(text_qury):
    tweets = []
    try:
        for tweet in api.search(q=text_qury, rpp=50, count=50):
            print(tweet.text)
            # adding to list that contains all tweets
            tweets.append({'created_at': tweet.created_at,
                           "tweet_id": tweet.id,
                           "tweet_text": tweet.text})
        return pd.DataFrame.from_dict(tweets)

        # print(tweets)
    except Exception as e:
        print("failed on a status", str(e))
        time.sleep(2)


# get_related_tweets("trump")
