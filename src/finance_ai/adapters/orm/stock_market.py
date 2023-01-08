from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    Float,
    String,
    Date,
    ForeignKey,
    event,
)
from sqlalchemy.orm import mapper, relationship
from finance_ai.domain.asset_db import stock_model

metadata = MetaData()

stock_daily_prices = Table(
    "stock_daily_prices",
    metadata,
    Column("date", Date, primary_key=True),
    Column("open", Float),
    Column("high", Float),
    Column("low", Float),
    Column("close", Float),
    Column("adj_close", Float),
    Column("volume", Float),
)


stocks = Table(
    "stocks",
    metadata,
    Column("market", ForeignKey("stock_markets.market")),
    Column("ticker", String(16), primary_key=True)
)

stock_markets = Table(
    "stock_markets",
    metadata,
    Column("market", String(16), primary_key=True),
)


def start_mappers():
    stock_daily_price_mapper = mapper(
        stock_model.StockDailyPrice, stock_daily_prices)
    
    stock_mapper = mapper(
        stock_model.Stock, stocks)
    
    stock_market_mapper = mapper(
        stock_model.StockMarket, 
        stock_markets,
        properties={
            "stocks": relationship(stock_mapper)
            })

@event.listens_for(stock_model.StockMarket, "load")
def receive_load(stock_market, _):
    stock_market.events = []