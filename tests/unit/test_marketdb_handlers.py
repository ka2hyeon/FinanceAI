import datetime 
import pandas as pd
import pytest

from ..fake_unit_of_work import FakeUnitOfWork
from portfolio import service_layer
from portfolio.domain import commands, events


def test_add_market():
    uow = FakeUnitOfWork()
    service_layer.add_market(uow, market='US')

    assert uow.markets.get(market='US').name == 'US'
    assert uow.committed


def test_reset_market_db():
    uow = FakeUnitOfWork()
    service_layer.reset_market(uow)


def test_update_krx_asset():
    uow = FakeUnitOfWork()
    service_layer.add_market(uow, market='krx')
    service_layer.update_assets(uow, market='krx')
    ret = uow.markets.get_asset_by_ticker(market='krx', ticker='005930')
    assert ret.name == '삼성전자'


def test_update_daily_market_price():
    uow = FakeUnitOfWork()
    service_layer.add_market(uow, market='krx')

    start_date = datetime.datetime.strptime('2022-01-01', '%Y-%m-%d').date()
    test_date = datetime.datetime.strptime('2022-01-03', '%Y-%m-%d').date()
    end_date= start_date+datetime.timedelta(days=60)

    service_layer.update_daily_market_prices(uow, market='krx', tickers=['005930'], 
                                            start_date=start_date, end_date=end_date)

    asset = uow.markets.get_asset_by_ticker(market='krx', ticker='005930')
    