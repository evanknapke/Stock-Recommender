# Stock-Predictor
Pulls live stock data through an api and suggests which stocks to buy or sell.

## Dependencies:
- Python 3+ (3.7.3 tested)
- Requests (`pip install requests`)

## How To

### Set up the config file:
1. Download/clone project
2. Open a terminal
3. cd into the Stock-Recommender directory
4. Run `touch config.ini` to create the config file
5. Open the config file `open config.ini` in an editor
6. Copy the following text to the config file:
```
[auth]
apikey=
symbols=
```
7. Retrieve an api key from [finnhub.io](https://finnhub.io/dashboard)
8. Copy and paste this key into the config file after `apikey=`
9. Add the stock tickers that you would like to evaluate separated by commas after `symbols=`
10. Your config.ini should look something like this:
```
[auth]
apikey=abc12de34f5ghijkl6mn
symbols=IBM, MSFT, TSLA, AAPL, F, GOOG
```
11. Save `config.ini`

### Run the program
1. Ensure that you cloned the project and have [set up the config file](#set-up-the-config-file)
2. Open a terminal
3. cd into the Stock-Recommender directory
4. Run `python stock-predictor.py`
