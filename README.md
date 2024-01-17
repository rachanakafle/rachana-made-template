## Correlation Analysis: COVID-19 Total Cases and Deaths in Asian and European Countries
This research project analyzes whether countries with more COVID-19 cases also have more death cases, aiming to determine if there's a strong correlation between the number of COVID-19 cases and death cases.

### Datasources
In this project, two Kaggle datasets are used. The first dataset contains COVID-19 cases in Asia as of October 10, 2021, and the second dataset provides COVID-19 data for Europe as of January 19, 2023.

 Datasource1: [Asia Covid 19 cases](https://www.kaggle.com/datasets/vivek468/asia-covid-19-cases-updated-10-oct-21/data)

Datasource2:[Europe Covid 19 cases](https://www.kaggle.com/datasets/anandhuh/latest-covid19-data-of-european-countries)

Kaggle data was accessed using personal credentials.

### Data pipeline 
The following data pipeline steps are followed.

**Data Collection:** 
Pulled datasets COVID-19 Asian and European countries datasets from Kaggle using the Kaggle API.

**Data Loading:** 
Loads the pulled datasets into pandas DataFrames.

**Data Transformation & Cleaning:**
Renames columns for the European COVID-19 dataset to make them consistent with the Asian COVID-19 dataset. Checking for missing or null values in both datasets and filling them with the mean where values are absent. Finally,selects only the relevant columns from both datasets.

**Data Storage:**
Stores the transformed Asian COVID-19 data into an SQLite database named asia_covid.sqlite. Similary,
Stores the transformed European COVID-19 data into an SQLite database named europe_covid.sqlite

### Final Report
The [Final report](https://github.com/rachanakafle/rachana-made-template/blob/main/project/report.ipynb) of this project is here.
