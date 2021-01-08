from configparser import ConfigParser
import json
import requests

def main():
    #retrieve user selected symbols from config.ini
    symbols = convert_to_list( get_from_config('symbols') )

    for symbol in symbols:
        paramaters = {
            "symbol": symbol,
            "resolution": "D",
            "from": 1583098857,
            "to": 1584308457,
            "indicator": "rsi",
            "timeperiod": 3,
            "token": get_from_config('apikey')
        }

        # api call
        rsi_response = requests.get('https://finnhub.io/api/v1/indicator?', params=paramaters)
        encoded_rsi = json.dumps(rsi_response.json(), sort_keys=True, indent=4) # json str
        decoded_rsi = json.loads(encoded_rsi) # json dict

        suggestion = check_rsi(decoded_rsi)
        print(symbol +": " + suggestion)

def check_rsi(json_data):
    rsi_list = json_data["rsi"]
    over_bought_threshold = 70.0
    over_sold_threshold = 30.0

    for rsi in rsi_list:
        if rsi < over_sold_threshold:
            suggestion = " buy"
        elif rsi > over_bought_threshold:
            suggestion = " sell"
        else:
            suggestion = " do nothing"

    return suggestion

# retrieves items from config.ini file by key
def get_from_config(key):
    config = ConfigParser()
    config.read('config.ini')
    return config.get('auth', key)

# converts string of comma seperated values to a list
def convert_to_list(string):
    cleaned_string = string.replace(" ", "")
    li = list(cleaned_string.split(","))
    return li

main()
