import urllib.request
import zipfile
import pandas as pd

# Download and unzip data
download_link = "https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip"
path = "mowesta-dataset-20221107.zip"
urllib.request.urlretrieve(download_link, path)
with zipfile.ZipFile(path, 'r') as zip_ref:
    zip_ref.extractall('mowesta-dataset-20221107')

# reading the data and selecting specific columns
df = pd.read_csv(
    "./mowesta-dataset-20221107/data.csv",
    delimiter=";",
    decimal=",",
    index_col=False,
    usecols=[
        "Geraet",
        "Hersteller",
        "Model",
        "Monat",
        "Temperatur in °C (DWD)",
        "Batterietemperatur in °C",
        "Geraet aktiv",
    ],
)  

# renaming columns
df = df.rename(
    columns={
        "Temperatur in °C (DWD)": "Temperatur",
        "Batterietemperatur in °C": "Batterietemperatur",
    }
)
# droping columns to the right of "Geraet aktiv"
df = df.loc[:, : "Geraet aktiv"]
#print(df.head())

# transform temperatures in Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

df["Temperatur"] = celsius_to_fahrenheit(df["Temperatur"])
df["Batterietemperatur"] = celsius_to_fahrenheit(df["Batterietemperatur"])

# validate data
column_types = {
    "Geraet": int,
    "Hersteller": str,
    "Model": str,
    "Monat": int,
    "Temperatur": float,
    "Batterietemperatur": float,
    "Geraet aktiv": str,
}
df = df.astype(column_types)
data_types = df.dtypes
print(data_types)

# Write to SQLite database
df.to_sql(
    "temperatures", "sqlite:///temperatures.sqlite", if_exists="replace", index=False
)