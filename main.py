from app.APIs.data_av import get_exchange_rate


if __name__ == '__main__':
    #print(get_data_monthy_adjusted('AAPL'))
    #print(get_data_daily_adjusted('AAPL'))
    #print(get_data_intraday('AAPL'))
    print(get_exchange_rate('USD', 'EUR'))  