import pandas as pd

INPUT_FILE = "netflix_titles.csv"
OUTPUT_FILE = "netflix_cleaned.csv"

# ============================================================
# STEP 1: IMPORT DATASET
# ============================================================
df = pd.read_csv(INPUT_FILE)

print("=" * 65)
print("STEP 1: IMPORT DATASET")
print("=" * 65)
print("Dataset imported successfully.")
print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())

# ============================================================
# STEP 2: IDENTIFY AND HANDLE MISSING VALUES
# ============================================================
print("\n" + "=" * 65)
print("STEP 2: MISSING VALUES")
print("=" * 65)

print("\nMissing values BEFORE cleaning:")
print(df.isnull().sum())

# Preserve records and clearly mark unavailable values.
missing_columns = [
    "director",
    "cast",
    "country",
    "date_added",
    "rating",
    "duration"
]

for column in missing_columns:
    if column in df.columns:
        df[column] = df[column].fillna("Unknown")

print("\nMissing values AFTER cleaning:")
print(df.isnull().sum())

# ============================================================
# STEP 3: DUPLICATES AND FORMATTING
# ============================================================
print("\n" + "=" * 65)
print("STEP 3: DUPLICATES AND FORMATTING")
print("=" * 65)

duplicates_before = df.duplicated().sum()
print("Duplicate rows before removal:", duplicates_before)

df = df.drop_duplicates().copy()

duplicates_after = df.duplicated().sum()
print("Duplicate rows after removal:", duplicates_after)

# Remove unnecessary whitespace from text fields.
text_columns = [
    "type", "title", "director", "cast", "country",
    "rating", "duration", "listed_in", "description"
]

for column in text_columns:
    if column in df.columns:
        df[column] = df[column].astype(str).str.strip()

print("Text formatting cleaned successfully.")

# ============================================================
# STEP 4: STANDARDIZE COUNTRY, RATING AND TYPE
# ============================================================
print("\n" + "=" * 65)
print("STEP 4: STANDARDIZATION")
print("=" * 65)

# Type: Movie / TV Show
df["type"] = df["type"].str.strip().str.title()

# Rating: consistent whitespace/capitalization
df["rating"] = df["rating"].str.strip().str.upper()

# Country: consistent whitespace around commas
df["country"] = (
    df["country"]
    .str.replace(r"\s*,\s*", ", ", regex=True)
    .str.strip()
)

# Create a simple country field for analysis.
df["primary_country"] = (
    df["country"]
    .str.split(",")
    .str[0]
    .str.strip()
)

print("\nStandardized Type values:")
print(df["type"].value_counts())

print("\nTop Rating values:")
print(df["rating"].value_counts().head(10))

print("\nTop Primary Country values:")
print(df["primary_country"].value_counts().head(10))

# ============================================================
# STEP 5: EXPORT CLEANED DATASET
# ============================================================
print("\n" + "=" * 65)
print("STEP 5: EXPORT CLEANED DATASET")
print("=" * 65)

df.to_csv(OUTPUT_FILE, index=False)

print("Cleaned dataset exported successfully.")
print("Output file:", OUTPUT_FILE)
print("Final shape:", df.shape)

print("\nProject completed successfully.")
