import abc
import datetime
from typing import Set

from finance_ai.domain.asset_db import stock_model

class StockMarketAbstractRepository(abc.ABC):
    def __init__(self):
        self.seen = set()  # type: Set[stock_model.StockMarket]

    def reset(self):
        self.seen = set()
        self._reset()

    def add(self, market: stock_model.StockMarket):
        self._add(market)
        self.seen.add(market)

    def get(self, exchange:str) -> stock_model.StockMarket:
        market = self._get(exchange)
        if market:
            self.seen.add(market)
        return market

    @abc.abstractmethod
    def _reset(self):
        pass

    @abc.abstractmethod
    def _add(self, stock_market: stock_model.StockMarket):
        raise NotImplementedError

    @abc.abstractmethod
    def _get(self, market:str) -> stock_model.StockMarket:
        raise NotImplementedError

    @abc.abstractmethod
    def _get_stock_daily_price(self, market, ticker) -> stock_model.StockDailyPrice:
        raise NotImplementedError


class StockMarketSqlAlchemyRepository(StockMarketAbstractRepository):
    def __init__(self, session):
        super().__init__()
        self.session = session

    def _reset(self):
        self.session.query(stock_model.StockMarket).delete()

    def _add(self, stock_market: stock_model.StockMarket):
        self.session.add(stock_market)

    def _get(self, market:str):
        return self.session.query(stock_model.StockMarket).filter_by(market=market)\
            .first()

    def _get_stock_daily_price(self, market, ticker):
        #TODO
        return self.session.query(stock_model.StockMarket).filter_by(market=market)\
            .first()