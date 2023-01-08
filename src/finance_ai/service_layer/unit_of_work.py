from __future__ import annotations
import abc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from finance_ai import config
from finance_ai.adapters import repository

class AbstractUnitOfWork(abc.ABC):
    stock_markets: repository.StockMarketAbstractRepository

    def __enter__(self) -> AbstractUnitOfWork:
        return self

    def __exit__(self, *args):
        self.rollback()

    def commit(self):
        self._commit()

    @abc.abstractmethod
    def _commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError

    def collect_new_events(self):
        for stock_market in self.stock_markets.seen:
            while stock_market.events:
                yield stock_market.events.pop(0)
        
DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=create_engine(
        config.get_mariadb_uri(),
        isolation_level="REPEATABLE READ",
    )
)

class SqlAlchemyUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session_factory=DEFAULT_SESSION_FACTORY):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()  # type: Session
        self.stock_markets = repository.StockMarketSqlAlchemyRepository(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def _commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()