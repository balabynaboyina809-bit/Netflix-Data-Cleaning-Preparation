# Netflix Data Cleaning & Preparation Using Python

## Project Overview

This project performs a complete **Netflix Data Cleaning & Preparation** workflow using **Python and Pandas**.

The purpose of this project is to clean, standardize, and prepare the Netflix dataset for further analysis and visualization while preserving records where information is unavailable.

The cleaning process includes importing the dataset, identifying and handling missing values, removing duplicate records, cleaning text formatting, standardizing selected fields, creating a simplified country field, and exporting the cleaned dataset.

---

## Workflow

The project follows five main steps:

1. **Import Dataset**
2. **Identify and Handle Missing Values**
3. **Remove Duplicates and Clean Formatting**
4. **Standardize Country, Rating, and Type**
5. **Export Cleaned Dataset**

---

## Technologies Used

* **Python**
* **Pandas**
* **CSV**
* **PyCharm IDE**

---

# Step 1: Import Dataset

The dataset is imported using the Pandas `read_csv()` function.

The program uses:

```python
INPUT_FILE = "Dataset_NotGiven_Empty.csv"
```

The dataset is then loaded into a Pandas DataFrame:

```python
df = pd.read_csv(INPUT_FILE)
```

After importing the dataset, the program displays:

* Dataset shape
* Column names
* First five rows

This provides an initial overview of the data before cleaning begins.

---

# Step 2: Identify and Handle Missing Values

The program first checks for missing values using:

```python
df.isnull().sum()
```

The following columns are specifically checked and cleaned:

```text
director
cast
country
date_added
rating
duration
```

Missing values in these columns are replaced with:

```text
Unknown
```

The following code performs the replacement:

```python
for column in missing_columns:
    if column in df.columns:
        df[column] = df[column].fillna("Unknown")
```

This approach preserves the records instead of deleting rows that contain missing information.

After the replacement, the program checks the dataset again to display the remaining missing values.

---

# Step 3: Duplicates and Formatting

## Duplicate Records

The program checks for duplicate rows before removing them:

```python
duplicates_before = df.duplicated().sum()
```

Duplicate records are then removed using:

```python
df = df.drop_duplicates().copy()
```

The program performs another duplicate check to confirm that duplicate rows have been removed.

---

## Text Formatting

Unnecessary whitespace is removed from relevant text fields.

The following columns are cleaned:

```text
type
title
director
cast
country
rating
duration
listed_in
description
```

The program uses:

```python
df[column] = df[column].astype(str).str.strip()
```

This ensures that leading and trailing spaces are removed from text values.

---

# Step 4: Standardization

The project standardizes three important fields:

* **Type**
* **Rating**
* **Country**

## Type Standardization

The `type` column is cleaned using:

```python
df["type"] = df["type"].str.strip().str.title()
```

This ensures consistent capitalization, such as:

```text
Movie
TV Show
```

---

## Rating Standardization

The `rating` column is standardized by removing unnecessary whitespace and converting values to uppercase:

```python
df["rating"] = df["rating"].str.strip().str.upper()
```

This creates a consistent format for rating values.

---

## Country Standardization

The `country` column is cleaned by standardizing whitespace around commas:

```python
df["country"] = (
    df["country"]
    .str.replace(r"\s*,\s*", ", ", regex=True)
    .str.strip()
)
```

For example, country values with inconsistent spacing around commas can be represented consistently as:

```text
United States, Canada, United Kingdom
```

---

## Creating the Primary Country Field

A new column called `primary_country` is created for easier analysis.

The first country listed in the `country` field is extracted:

```python
df["primary_country"] = (
    df["country"]
    .str.split(",")
    .str[0]
    .str.strip()
)
```

For example:

| country               | primary_country |
| --------------------- | --------------- |
| United States, Canada | United States   |
| United Kingdom        | United Kingdom  |
| India, United States  | India           |

This provides a simple country field that can be used for analysis and visualization.

---

## Standardization Results

The program displays the standardized values for:

### Type

```python
print(df["type"].value_counts())
```

### Rating

```python
print(df["rating"].value_counts().head(10))
```

### Primary Country

```python
print(df["primary_country"].value_counts().head(10))
```

These summaries provide an overview of the cleaned categorical data.

---

# Step 5: Export Cleaned Dataset

After completing the cleaning and standardization process, the final dataset is exported as a CSV file.

The output file is:

```python
OUTPUT_FILE = "netflix_cleaned.csv"
```

The cleaned DataFrame is saved using:

```python
df.to_csv(OUTPUT_FILE, index=False)
```

The program then displays the output filename and the final dataset shape.

---

# Input and Output Files

### Input File

```text
Dataset.csv
```

### Output File

```text
netflix_cleaned.csv
```

The output file contains the cleaned and standardized dataset, including the newly created:

```text
primary_country
```

column.

---

# Data Cleaning Summary

| Cleaning Task     | Action                                          |
| ----------------- | ----------------------------------------------- |
| Missing values    | Replaced selected missing values with `Unknown` |
| Duplicate records | Removed duplicate rows                          |
| Text formatting   | Removed leading and trailing whitespace         |
| Type              | Standardized using title case                   |
| Rating            | Standardized using uppercase                    |
| Country           | Standardized comma spacing                      |
| Primary country   | Created from the first country listed           |
| Export            | Saved as `netflix_cleaned.csv`                  |

---

# Final Result

The project successfully prepares the Netflix dataset for further analysis and visualization.

The final cleaned dataset:

* Preserves records containing unavailable information.
* Replaces selected missing values with `Unknown`.
* Removes duplicate records.
* Cleans unnecessary whitespace.
* Standardizes `type`, `rating`, and `country`.
* Creates a new `primary_country` field.
* Exports the cleaned data to `netflix_cleaned.csv`.

The complete workflow provides a structured and reproducible approach to preparing the Netflix dataset using Python and Pandas.
