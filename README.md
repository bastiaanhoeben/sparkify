## Sparkify data modeling with PostgreSQL

### About the project
In this project, data from a fictive streaming music company "Sparkify" is 
processed and written to a PostgreSQL database. The data is hereby modelled 
to fit a snowflake schema. This project is part of the Udacity nanodegree 
Data Engineering.

### Overview

The project contains three Python scripts, being:

- **sql_queries.py**, containing all the SQL queries performed on the Postgres 
  database engine;
- **create_tables.py**, containing functions for creating a new database 
  schema and creating the necessary fact table and dimension tables; and
- **etl.py**, containing functions for extracting song and log data from 
  files, transforming said data to adhere to the data model and writing said 
  transformed data to the relational database.

In addition, the repo provides data for testing purposes, provided in the 
*data* directory. Said data comprises both user log files and files containing 
song metadata.

Finally, two Jupyter Notebook files are provided for testing purposes, being:

- **test.ipynb**, containing python code to test proper creation of the 
  database tables; and
- **etl.ipynb**, containing skeleton code on which the *etl.py* script is based.

### Getting started

To get an environment running on your system in which to create the ETL 
pipelines, go through the following steps:

1. Clone the repository into the working directory and move into the project
   directory:
   ```
   git clone https://github.com/bastiaanhoeben/sparkify.git
   ```
   ```
   cd sparkify
   ```   
 
2. Start up the PostgreSQL database service in the background:
   ```
   docker-compose up -d
   ```

2. Create a virtual environment and activate it:
   ```
   python3 -m venv .venv
   ```
   ```
   source .venv/bin/activate
   ```
   
4. Install the necessary packages from requirements.txt:
   ```
   python -m pip install -r requirements.txt
   ```

5. Create database schema and tables with the *create_tables.py* script:
   ```
   python create_tables.py
   ```
   
6. Run the pipelines with the *etl.py* script:
   ```
   python etl.py
   ```

### Making use of the Jupyter notebooks

The database can be populated without the use of the notebooks. For a proper 
functioning of the notebooks, Jupyter Notebook must run *inside* the virtual 
environment. An easy way to achieve this is by installing Jupyter Notebook 
within the activate venv like so:
```
pip install notebook
```

The notebooks can then be started easily through:
```
jupyter notebook test.ipynb
jupyter notebook etl.ipynb
```