import opendatasets as od
import pandas as pd
#download covid-19 asian countries dataset
od.download(
	"https://www.kaggle.com/datasets/vivek468/asia-covid-19-cases-updated-10-oct-21/data")

# download covid-19 european countries dataset
od.download(
	"https://www.kaggle.com/datasets/anandhuh/latest-covid19-data-of-european-countries")


# Read the asia covid data
file_path = 'asia-covid-19-cases-updated-10-oct-21/AsiaCases_.csv'
df_asia_covid = pd.read_csv(file_path)
print(df_asia_covid.head())

# Read the europe covid data
file_path = 'latest-covid19-data-of-european-countries/europe_covid.csv'
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
selected_columns = ["Country","Total Cases","Total Deaths","Total Recovered","Active Cases","Total Tests","Population"]

# Create a new DataFrame with only the selected columns
new_df_asia_covid  = df_asia_covid [selected_columns]
print(new_df_asia_covid.head())
new_df_europe_covid =df_europe_covid[selected_columns]
print(new_df_europe_covid.head())



