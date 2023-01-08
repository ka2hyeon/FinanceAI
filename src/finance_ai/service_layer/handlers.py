from __future__ import annotations
from typing import TYPE_CHECKING

from finance_ai.adapters import email
from finance_ai.domain import commands, events
from finance_ai.domain.asset_db import stock_model

if TYPE_CHECKING:
    from . import unit_of_work


class InvalidReport(Exception):
    pass


def add_stock_market(
    cmd: commands.AddStockMarket,
    uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        market = uow.stock_markets.get(cmd.market)
        if market is None:
            stock_market = stock_model.StockMarket(market=cmd.market, 
                                                    stocks=[])
            uow.stock_markets.add(stock_market)
        else:
            raise Exception("Market already exists")
        uow.commit()

def get_stock_market(
    cmd: commands.GetStockMarket,
    uow: unit_of_work.AbstractUnitOfWork):
    with uow:
        market = uow.stock_markets.get(cmd.market)
    return market


def send_email(
    event: events.StockMarketAdded,
    uow: unit_of_work.AbstractUnitOfWork,
):
    email.send(
        "ka2hyeon@gmail.com",
        f"{event.market} is added",
    )

