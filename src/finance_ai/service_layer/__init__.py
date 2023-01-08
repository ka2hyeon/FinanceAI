from . import messagebus, unit_of_work
from ..domain import commands, events

def get_uow():
    return unit_of_work.SqlAlchemyUnitOfWork()

def add_stock_market(uow, market):
    messagebus.handle(
        commands.AddStockMarket(
            market=market,
            symbol=symbol,
            name=name
        ), uow
    )
