from decouple import config
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.foreignexchange import ForeignExchange

#variable global
av_api_key = config('AV_API_KEY')

ts = TimeSeries(key=av_api_key, output_format='pandas')

def get_data_monthy_adjusted(symbol):
    data = ts.get_monthly_adjusted(symbol=symbol)
    return data[0]

def get_data_daily_adjusted(symbol):
    data = ts.get_daily_adjusted(symbol=symbol)
    return data[0]

def get_data_intraday(symbol):
    data = ts.get_intraday(symbol=symbol, interval='5min')
    return data[0]

def get_exchange_rate(from_currency, to_currency):
    fe = ForeignExchange(key=av_api_key)
    data, _ = fe.get_currency_exchange_rate(from_currency=from_currency, to_currency=to_currency)
    return data

if __name__ == '__main__':
    #print(get_data_monthy_adjusted('AAPL'))
    #print(get_data_daily_adjusted('AAPL'))
    #print(get_data_intraday('AAPL'))
    print(get_exchange_rate('USD', 'EUR'))