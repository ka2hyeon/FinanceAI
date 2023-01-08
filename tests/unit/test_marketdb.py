import datetime
from portfolio.domain import marketdb


def test_krx_update_assets():
    market = marketdb.Market(name='KR')
    market.update_assets()

    samsung = [a for a in market.assets if a.ticker=='005930'][0]
    assert samsung.name == '삼성전자'


def test_krx_update_price():
    market = marketdb.Market(name='KR')
    market.update_assets()
    
    start_date = datetime.datetime.strptime('2022-01-01', '%Y-%m-%d').date()
    test_date = datetime.datetime.strptime('2022-01-03', '%Y-%m-%d').date()
    end_date= start_date+datetime.timedelta(days=60)

    samsung = [a for a in market.assets if a.ticker=='005930'][0]
    today= datetime.date.today()
    samsung.update_prices(start_date=start_date, end_date=end_date)

    price = [p for p in samsung.prices if p.date==test_date][0]
    assert price.close == 78600


def test_krx_update_price_by_specific_ticker_and_date():
    market = marketdb.Market(name='KR')
    market.update_assets()
    
    start_date = datetime.datetime.strptime('2022-01-01', '%Y-%m-%d').date()
    test_date = datetime.datetime.strptime('2022-01-03', '%Y-%m-%d').date()
    end_date= start_date+datetime.timedelta(days=60)

    market.update_prices(
        tickers = ['005930'],
        start_date = start_date,
        end_date = end_date
    )
    
    samsung = [a for a in market.assets if a.ticker=='005930'][0]
    price = [p for p in samsung.prices if p.date==test_date][0]
    assert price.close == 78600
