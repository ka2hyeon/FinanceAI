import argparse
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../src")

from sqlalchemy import create_engine

from finance_ai import config
from finance_ai import service_layer
from finance_ai.adapters import orm
from finance_ai.domain import commands, events


def parse_args():
    parser = argparse.ArgumentParser()
    return parser.parse_args() 


if __name__ == '__main__':
    args = parse_args()
    engine = create_engine(config.get_mariadb_uri())
    engine.connect()

    orm.start_mappers()
    orm.create_all(engine)
    uow = service_layer.get_uow()


    service_layer.messagebus.handle(
        commands.AddStockMarket(market='test'),
        uow
    )

    service_layer.messagebus.handle(
        commands.GetStockMarket(market='test'),
        uow
    )

    import IPython; IPython.embed()