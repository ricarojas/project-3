# Project 3 - Data Visulations on Prevelance of Disablity in Australia

### Approach

1. Find data source for Prevelance of Disabilities.
2. Extract data from website of choice see **Data Sources** section of this document.
3. Massage the data. Needed to take the xls, transform it to a .csv using Numbers. This split the sheets into individual csv files.
4. Using python and pandas to cleanup the data, and remove any unwated headings.
5. Using pandas to output the clean data to a new csv for upload to MongoDB.
6. Using the command line and mongoimport to import the new csv to MongoDB. Commands can be found in the **Importing data into MongoDB** section of this file.

### Technologies Used

- Python
- MongoDb
- Python Flask
- HTML / CSS

### Data Sources

- https://www.abs.gov.au/statistics/health/disability/disability-ageing-and-carers-australia-summary-findings/latest-release#data-downloads

### Tools Used

- MongoDb Compass : To help visualise data imported into the databse.

### Importing data into MongoDB

mongoimport -d australian_disability --collection nsw_data_2012 --file nsw_disability_2012_data.csv --type csv --headerline
