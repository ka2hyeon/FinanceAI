import json
import random
import uuid
from datetime import datetime, date, timedelta

from finance_ai.domain.asset_db import stock_model 

def random_stock_daily_prices()->stock_model.StockDailyPrice:
    random_stock_daily_price = stock_model.StockDailyPrice(
        date=date.today(),
        open=random.uniform(1,100000),
        high=random.uniform(open,100000),
        low=random.uniform(1,open),
        close=random.uniform(low,high),
        adj_close=random.uniform(1,100000),
        volume=random.uniform(1,100000),
    )
    return random_stock_daily_price