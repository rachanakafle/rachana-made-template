
import os
import sqlite3
import pandas as pd
import pytest
from pipeline import asia_europe_db

def test_asia_europe_data():
    asia_europe_db()

    # Check if the SQLite database is created or not
    assert os.path.isfile('./data/asia_covid.sqlite')
