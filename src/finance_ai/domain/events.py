import datetime
from dataclasses import dataclass

class Event:
    pass


@dataclass
class StockMarketAdded(Event):
    market: str