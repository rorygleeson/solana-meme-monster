import json
import requests
import tweepy
import boto3


def get_twitter_keys():
    """Retrieve secrets from Parameter Store."""
    print("Get Keys")
    # Create our SSM Client.
    aws_client = boto3.client('ssm')

    # Get our keys from Parameter Store.
    parameters = aws_client.get_parameters(
        Names=[
            'twitter_api_key',
            'twitter_api_secret',
            'twitter_access_token',
            'twitter_access_secret',
            'twitter_bearer_code'
        ],
        WithDecryption=True
    )
    
    # Convert list of parameters into simpler dict.
    keys = {}
    for parameter in parameters['Parameters']:
        keys[parameter['Name']] = parameter['Value']

    return keys
    


def lambda_handler(event, context):


    keys = get_twitter_keys()
    print("Search Twitter")
    client = tweepy.Client(
        bearer_token=keys.get('twitter_bearer_code')
    )

   
    """
    If you don't understand search queries, there is an excellent introduction to it here: 
    https://github.com/twitterdev/getting-started-with-the-twitter-api-v2-for-academic-research/blob/main/modules/5-how-to-write-search-queries.md
    """
   
    # Get tweets that contain the hashtag #petday
    # -is:retweet means I don't want retweets
    # lang:en is asking for the tweets to be in english
    query = '#petday -is:retweet lang:en'
    tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100)
    
    
    """
    What context_annotations are: 
    https://developer.twitter.com/en/docs/twitter-api/annotations/overview
    """
   
    for tweet in tweets.data:
        print(tweet.text)
        if len(tweet.context_annotations) > 0:
            print(tweet.context_annotations)
   
   
    return {
        "statusCode": 200,
        "body": json.dumps({
            "crawlStart": "Go CrawlerFunction",
        }),
    }
