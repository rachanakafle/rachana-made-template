import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import *
import re

# step1: fetch the csv data from the provided url
data_url = "https://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2020_alle.CSV"

# step2: read csv data into Dataframe
df = pd.read_csv(data_url,delimiter=';')
print(df.head())

# Requirement 1: Drop the "Status" Column
df = df.drop(columns=['Status'])

# Requirement 2: validation
df['Laenge'] = df['Laenge'].str.replace(r',', '.').astype(float)
df['Breite'] = df['Breite'].str.replace(r',', '.').astype(float)
df = df[df['Verkehr'].isin(['FV', 'nur DPN', 'RV'])]
df = df[ (df['Laenge'] <= 90) & (df['Laenge'] >= -90)]
df = df[ (df['Breite'] <= 90) & (df['Breite'] >= -90)]
pattern = re.compile(r"^\w{2}:\d+:\d+(?::\d+)?$")
valid_ifopt = df["IFOPT"].astype(str).str.contains(pattern, regex=True)
df = df.loc[valid_ifopt]
#drop rows with empty cells
df = df.dropna()

# Define columns datatypes
columns_types = {
    "DS100": TEXT,
    "EVA_NR": Integer,
    "Laenge": FLOAT,
    "Breite": FLOAT,
    "Verkehr": Text,
    "IFOPT": Text,
    "NAME": Text,
    "Betreiber_Name": Text,
    "Betreiber_Nr": Integer

}
# Step 3: Data Loading
table_names = "trainstops"
connection=create_engine("sqlite:///trainstops.sqlite", echo=True)

# Write the DataFrame to SQLite database
df.to_sql(table_names, connection, if_exists='replace',index=False,dtype=columns_types)




