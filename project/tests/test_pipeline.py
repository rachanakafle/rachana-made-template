import os
from pipeline import asia_europe_db


def test_asia_data():
    asia_europe_db()
    # Check if the asia_covid.sqlite database is created or not
    assert os.path.isfile('./data/asia_covid.sqlite')

def test_europe_data():
    asia_europe_db()
    # Check if the europe_covid.sqlite database is created or not
    assert os.path.isfile('./data/europe_covid.sqlite')
