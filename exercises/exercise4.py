import urllib.request
import zipfile
import pandas as pd

# Download and unzip data
download_link = "https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip"
path = "mowesta-dataset-20221107.zip"
urllib.request.urlretrieve(download_link, path)
with zipfile.ZipFile(path, 'r') as zip_ref:
    zip_ref.extractall('mowesta-dataset-20221107')

#reading the data and selecting specific columns
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
##