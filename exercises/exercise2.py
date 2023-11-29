import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import *
import re

# step1: fetch the csv data from the provided url
data_url = "https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV"

# step2: read csv data into Dataframe
df = pd.read_csv(data_url,delimiter=';')
print(df.head())
