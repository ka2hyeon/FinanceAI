import datetime
import pandas as pd
from typing import Optional, List
from dataclasses import dataclass


class Command:
    pass

@dataclass
class AddStockMarket(Command):
    market: str

@dataclass
class GetStockMarket(Command):
    market: str


