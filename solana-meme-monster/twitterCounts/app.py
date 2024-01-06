import json
import tweepy
# import requests

def get_twitter_keys():
    """Retrieve secrets from Parameter Store."""
    # Create our SSM Client.
    aws_client = boto3.client('ssm')

    # Get our keys from Parameter Store.
    parameters = aws_client.get_parameters(
        Names=[
            'twitter_api_key',
            'twitter_api_secret',
            'twitter_access_token',
            'twitter_access_secret'
        ],
        WithDecryption=True
    )

    # Convert list of parameters into simpler dict.
    keys = {}
    for parameter in parameters['Parameters']:
        keys[parameter['Name']] = parameter['Value']

    return keys



def get_tweet():
    """Creates our tweet."""

  
    tweet = "WTF5673"
    return tweet




def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e


    keys = get_twitter_keys()

    client = tweepy.Client(
        consumer_key=keys.get('twitter_api_key'),
        consumer_secret=keys.get('twitter_api_secret'),
        access_token=keys.get('twitter_access_token'),
        access_token_secret=keys.get('twitter_access_secret')
    )

    tweet = get_tweet()
    client.create_tweet(text=tweet)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Tweet Sent? BONK token mentions in last hour = 34219",
            # "location": ip.text.replace("\n", "")
        }),
    }
