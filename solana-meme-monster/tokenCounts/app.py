import json
# import requests


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
    

    # python object(dictionary) to be dumped 
    tokenCount ={ 
        "$BONK": { 
            "twitter": "9999", 
            "tiktok": "213", 
            "youtube": "23",
            "reddit" : "154",
            "discord" : "233",
            "instagram": "34"
        }, 
        "$DOGWIFHAT": { 
            "twitter": "3211", 
            "tiktok": "213", 
            "youtube": "23",
            "reddit" : "154",
            "discord" : "233",
            "instagram": "34"
        },
        "$ANALOS": { 
            "twitter": "3211", 
            "tiktok": "213", 
            "youtube": "23",
            "reddit" : "154",
            "discord" : "233",
            "instagram": "34"
        }, 
        "$SILLYDRAGON": { 
            "twitter": "3211", 
            "tiktok": "213", 
            "youtube": "23",
            "reddit" : "154",
            "discord" : "233",
            "instagram": "34"
        },
        "$SoBIT": { 
            "twitter": "3211", 
            "tiktok": "213", 
            "youtube": "23",
            "reddit" : "154",
            "discord" : "233",
            "instagram": "34"
        }, 
        "$LessFnGas": { 
            "twitter": "3211", 
            "tiktok": "213", 
            "youtube": "23",
            "reddit" : "154",
            "discord" : "233",
            "instagram": "34"
        },
        "$USEDCAR": { 
            "twitter": "3211", 
            "tiktok": "213", 
            "youtube": "23",
            "reddit" : "154",
            "discord" : "233",
            "instagram": "34"
        }, 
        "$POPCAT": { 
            "twitter": "3211", 
            "tiktok": "213", 
            "youtube": "23",
            "reddit" : "154",
            "discord" : "233",
            "instagram": "34"
        },
    } 

    return {
        "statusCode": 200,
        "body": json.dumps(tokenCount)
    }
    
