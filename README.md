Netflix Data Cleaning & Preparation Using Python
Project Overview
This project completes the five-step Netflix Data Cleaning & Preparation workflow using Python and Pandas.
Workflow
1. Import the Netflix dataset using Python and Pandas.
2. Identify and handle missing values.
3. Remove duplicate records and formatting inconsistencies.
4. Standardize Country, Rating, and Type.
5. Export the cleaned dataset for further analysis.
Dataset
The project uses the commonly used Netflix Movies and TV Shows dataset (netflix_titles.csv), containing 8,807 records and 12 original columns.
Expected original columns:
show_id
type
title
director
cast
country
date_added
release_year
rating
duration
listed_in
description
Step 1 — Import the Dataset
The Python program uses Pandas:
import pandas as pd

df = pd.read_csv("netflix_titles.csv")
The expected original shape is:
Rows: 8,807
Columns: 12
The program prints the first five records and column names so the structure can be checked.
Step 2 — Identify and Handle Missing Values
The program checks missing values with:
df.isnull().sum()
Missing values in the standard dataset occur mainly in:
- director
- cast
- country
- date_added
- rating
- duration
Instead of deleting thousands of records, unavailable text/categorical values are replaced with:
Unknown
This keeps the records available for later analysis.
Step 3 — Remove Duplicates and Formatting Inconsistencies
Duplicate records are checked using:
df.duplicated().sum()
Then duplicates are removed with:
df = df.drop_duplicates()
Text columns are stripped of leading and trailing whitespace:
df[column] = df[column].astype(str).str.strip()
Step 4 — Standardize Country, Rating and Type
Type
Values are standardized to:
Movie
TV Show
Country
Whitespace around commas is standardized, and a primary_country column is created from the first listed country.
Rating
Rating values are stripped and converted to a consistent uppercase format.
Step 5 — Export the Cleaned Dataset
The final cleaned dataset is exported with:
df.to_csv("netflix_cleaned.csv", index=False)
The cleaned file can then be used for exploratory data analysis, visualization and further Python projects.
Expected Results
The standard dataset starts with:
8,807 rows
12 columns
There are no exact duplicate rows in the standard dataset.
After cleaning, all missing values handled by the script are represented by Unknown.
The script adds:
primary_country
Therefore the final analysis dataset contains:
8,807 rows
13 columns
Files in This GitHub Repository
File	Purpose
README.md	Step-by-step project explanation
netflix_data_cleaning.py	Complete Python program
project_outputs.txt	Console outputs/results
requirements.txt	Python libraries required


How to Run
1. Download or clone this repository.
2. Put netflix_titles.csv in the same folder as the Python file.
3. Install the required packages:
pip install -r requirements.txt
4. Run:
python netflix_data_cleaning.py
5. The program creates:
netflix_cleaned.csv
Important Note
The numerical results in project_outputs.txt describe the commonly used 8,807-row Netflix titles dataset. If a different version of the dataset is supplied, row counts or missing-value counts may differ.
