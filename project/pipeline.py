# import opendatasets as od
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi
import sqlite3
def asia_europe_db():
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files('vivek468/asia-covid-19-cases-updated-10-oct-21/', 'project/asia-covid-19-cases-updated-10-oct-21', unzip=True)
    api.dataset_download_files('anandhuh/latest-covid19-data-of-european-countries', 'project/latest-covid19-data-of-european-countries', unzip=True)
    # Read the asia covid data
    file_path = 'project/asia-covid-19-cases-updated-10-oct-21/AsiaCases_.csv'
    df_asia_covid = pd.read_csv(file_path)
    print(df_asia_covid.head())
    # Read the europe covid data
    file_path = 'project/latest-covid19-data-of-european-countries/europe_covid.csv'
    df_europe_covid = pd.read_csv(file_path)
    print(df_europe_covid.head())

    # select only relevent columns
    '''
    Country
    Total Cases
    Total Deaths
    Total Recovered
    Active Cases
    Total Tests
    Population
    '''
    # Select relevant columns
    selected_columns_asia = ["Country","TotalCases","TotalDeaths","TotalRecovered","ActiveCases","TotalTests"]
    selected_columns_europe = ["Country/Other","Total Cases","Total Deaths","Total Recovered","Active Cases","Total Tests"]

    # Create a new DataFrame with only the selected columns
    new_df_asia_covid  = df_asia_covid [selected_columns_asia]
    print(new_df_asia_covid.head())
    new_df_europe_covid = df_europe_covid[selected_columns_europe]
    data_types_asia ={"Country":"TEXT",
                "TotalCases":"INTEGER",
                "TotalDeaths":"INTEGER",
                "TotalRecovered":"INTEGER",
                 "ActiveCases":"INTEGER",
                 "TotalTests":"INTEGER"}

    data_types_europe = {"Country/Other": "TEXT",
                       "Total Cases": "INTEGER",
                       "TotalD eaths": "INTEGER",
                       "Total Recovered": "INTEGER",
                       "Active Cases": "INTEGER",
                       "Total Tests": "INTEGER"}

    conn1 = sqlite3.connect('./data/asia_covid.sqlite')
    new_df_asia_covid.to_sql('asia', conn1, index=False, if_exists='replace', dtype=data_types_asia)
    conn1.close()

    conn2 = sqlite3.connect('./data/asia_covid.sqlite')
    new_df_asia_covid.to_sql('asia', conn2, index=False, if_exists='replace', dtype=data_types_europe)
    conn2.close()
