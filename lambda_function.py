import random
import json

def lambda_handler(event, context):
    question = event.get('queryStringParameters', {}).get('question','')
    fortune = get_fortune()

    return {
        'statusCode':200,
        'body': json.dumps({
            'question': question,
            'fortune': fortune
        })
    }

def get_fortune():
    num = random.randint(1, 3)
    if num == 1:
        return "Yes"
    elif num == 2:
        return "No"
    else:
        return "Maybe"