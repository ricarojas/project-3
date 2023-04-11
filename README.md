# Project 3 - Data Visulations on Prevelance of Disablity in Australia

### Approach

1. Find data source for Prevelance of Disabilities.
2. Extract data from the chosen website **Data Sources** section of this document.

- After extraction open the .xls in Numbers and using the export function to generate individual files
  for each of the tables. Focusing on Table_1.1-Table 1
- Renamed them to their appropriate states for easier referencing.

3. Massage the data. Needed to take the xls, transform it to a .csv using Numbers. This split the sheets into individual csv files.
4. Using python and pandas to cleanup the data, and remove any unwated headings / other unwanted infromation.

- run each of the clean*up*\*.ipynb to generate the CleanData files again.

5. Using the command line and mongoimport to import the new csv to MongoDB. Commands can be found in the **Importing data into MongoDB** section of this file.
6. Check data using check_data.ipynb simply confirms data has been created and is accesible.

If you would like to run this locally, please see the section **Running FLASK**

### Languages and Technologies Used

- Python
- MongoDb
- Python Flask
- HTML / CSS
- Javascript

### Data Sources

- https://www.abs.gov.au/statistics/health/disability/disability-ageing-and-carers-australia-summary-findings/latest-release#data-downloads
- NSW : https://www.abs.gov.au/statistics/health/disability/disability-ageing-and-carers-australia-summary-findings/2018/44300do001_2018.xls
- VIC : https://www.abs.gov.au/statistics/health/disability/disability-ageing-and-carers-australia-summary-findings/2018/44300do002_2018.xls
- QLD : https://www.abs.gov.au/statistics/health/disability/disability-ageing-and-carers-australia-summary-findings/2018/44300do003_2018.xls
- SA : https://www.abs.gov.au/statistics/health/disability/disability-ageing-and-carers-australia-summary-findings/2018/44300do004_2018.xls
- WA : https://www.abs.gov.au/statistics/health/disability/disability-ageing-and-carers-australia-summary-findings/2018/44300do005_2018.xls
- TAS : https://www.abs.gov.au/statistics/health/disability/disability-ageing-and-carers-australia-summary-findings/2018/44300do006_2018.xls

### Tools Used

- MongoDb Compass : To help visualise data imported into the databse
- Numbers (Mac Excel Equivelant) : To help split out the tables

### Importing data into MongoDB

mongoimport -d australian_disability --collection state_and_year --file nsw_disability_data.csv --type csv --headerline
mongoimport -d australian_disability --collection state_and_year --file vic_disability_data.csv --type csv --headerline
mongoimport -d australian_disability --collection state_and_year --file qld_disability_data.csv --type csv --headerline
mongoimport -d australian_disability --collection state_and_year --file sa_disability_data.csv --type csv --headerline
mongoimport -d australian_disability --collection state_and_year --file wa_disability_data.csv --type csv --headerline
mongoimport -d australian_disability --collection state_and_year --file tas_disability_data.csv --type csv --headerline

### Running FLASK

- May have to set the environment variables using and then run
  export FLASK_APP=app
  export FLASK_ENV=development
  flask run --port 8000

You should now be able to view this application on

- localhost:8000 (on Windows)
- 127.0.0.1:8000 (on Mac)

### Challenges

- The data from ABS needed to be massaged, remove logos and other lines that were not relevant.
- No data for the Northern Territory.
- Australian Captial Territory didn't have data in the same format with regards to the age brackets and gender.
