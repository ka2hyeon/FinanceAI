from datetime import datetime, date
from portfolio.domain import gurudb


def test_update_gurudb():
    cik = '0001029160'
    name = "George Soros"
    nickname = ''

    #cik = '0001600319'
    #name = 'Bridgewater Advisors Inc.'
    #nickname = ''

    start_date = datetime.strptime('2021-01-01', '%Y-%m-%d').date()
    end_date = datetime.strptime('2021-12-31', '%Y-%m-%d').date()

    guru = gurudb.Guru(cik, name, nickname, guru_reports=[])
    guru.update(start_date, end_date)


