import requests 

def get_data():
    parameters = {
    "amount": 10,
    "type": "boolean",

    }

    response = requests.get(url="https://opentdb.com/api.php", params = parameters)
    response.raise_for_status()
    data = response.json()
    question_data = data["results"]
    return question_data