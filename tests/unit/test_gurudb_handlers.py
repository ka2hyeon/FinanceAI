import pandas as pd
import pytest

from datetime import datetime, date

from ..fake_unit_of_work import FakeUnitOfWork
from portfolio import service_layer 
from portfolio.domain import commands, events


def test_add_guru():
    uow = FakeUnitOfWork()
    cik = '0000315090' 
    name = 'Buffett Warren E'
    nickname = 'Buffett'
    
    service_layer.add_guru(uow, cik, name, nickname)
    assert uow.gurus.get(cik).name == 'Buffett Warren E'
    assert uow.committed


def test_update_gurudb():
    cik = "0001029160"
    name = "George Soros"
    nickname = "George Soros"
    start_date = datetime.strptime('2021-01-01', '%Y-%m-%d').date()
    end_date = datetime.strptime('2021-12-31', '%Y-%m-%d').date()

    uow = FakeUnitOfWork()
    service_layer.add_guru(uow, cik, name, nickname)
    service_layer.update_guru(uow, cik, start_date, end_date)
    
    assert len(uow.gurus.get(cik).reports) != 0
    assert uow.committed