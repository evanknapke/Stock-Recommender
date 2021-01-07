from configparser import ConfigParser
from datetime import datetime, timedelta
import json
import requests

def main():
    #TODO: check rsi of each symbol in selected list
    #      (alphavantage might already have something set up for this)
    rsi_paramaters = {
        "function": "RSI",
        "symbol": "IBM",
        "interval": "weekly",
        "time_period": 10,
        "series_type": "open",
        "apikey": get_from_config('apikey')
    }

    # api call
    rsi_response = requests.get('https://www.alphavantage.co/query?', params=rsi_paramaters)

    encoded_rsi = json.dumps(rsi_response.json(), sort_keys=True, indent=4) # json str
    decoded_rsi = json.loads(encoded_rsi) # json dict

    try: # try to find latest possible data
        today = datetime.today().strftime('%Y-%m-%d')
        print( check_rsi(decoded_rsi, today) )
    except KeyError: # todays date may not be available yet
        yesterday = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')
        print( check_rsi(decoded_rsi, yesterday) )


def check_rsi(json_data, date):
    rsi = float( json_data["Technical Analysis: RSI"][date]["RSI"] )
    over_bought_threshold = 70.0
    over_sold_threshold = 30.0

    if rsi < over_sold_threshold:
        return "buy"
    elif rsi > over_bought_threshold:
        return "sell"
    else:
        return "do nothing"

# retrieves items from config.ini file by key
def get_from_config(key):
    config = ConfigParser()
    config.read('config.ini')
    return config.get('auth', key)


main()
