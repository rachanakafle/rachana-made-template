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
    selected_columns = ["Country","TotalCases","TotalDeaths","TotalRecovered","ActiveCases","TotalTests"]

    # Create a new DataFrame with only the selected columns
    new_df_asia_covid  = df_asia_covid [selected_columns]
    print(new_df_asia_covid.head())

    #new_df_europe_covid =df_europe_covid[selected_columns]
    #print(new_df_europe_covid.head())
    data_types ={"Country":"TEXT",
                "TotalCases":"INTEGER",
                "TotalDeaths":"INTEGER",
                "TotalRecovered":"INTEGER",
                 "ActiveCases":"INTEGER",
                 "TotalTests":"INTEGER"}

    conn = sqlite3.connect('./data/asia_covid.sqlite')
    new_df_asia_covid.to_sql('asia', conn, index=False, if_exists='replace', dtype=data_types)
    conn.close()
