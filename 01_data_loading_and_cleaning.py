# Step 1: Data Loading and Cleaning
# This script loads the movie reviews dataset and cleans it

import pandas as pd
import re

# Load the raw data from excel file
print("Loading dataset...")
df = pd.read_excel("movie_reviews_10000_varied_titles.xlsx")

print("Dataset shape:", df.shape)
print("Columns:", list(df.columns))
print()

# Display first few rows to understand the data
print("First 5 rows:")
print(df.head())
print()

# --- Data Cleaning ---

# 1. Check for missing values
print("Checking for missing values...")
print(df.isnull().sum())
print()

missing = df.isnull().sum().sum()
if missing > 0:
    print(f"Found {missing} missing values. Dropping those rows...")
    df = df.dropna()
else:
    print("No missing values found!")
print()

# 2. Check for duplicate rows
duplicates = df.duplicated().sum()
print(f"Duplicate rows found: {duplicates}")
if duplicates > 0:
    df = df.drop_duplicates()
    print("Duplicates removed.")
print()

# 3. Clean the review text
# - convert to lowercase
# - remove extra spaces
# - remove special characters
print("Cleaning review text...")
df['review_tweet'] = df['review_tweet'].astype(str).str.strip()
df['review_tweet'] = df['review_tweet'].str.lower()
df['review_tweet'] = df['review_tweet'].apply(lambda x: re.sub(r'[^a-z0-9\s.,!?\'-]', '', x))
df['review_tweet'] = df['review_tweet'].apply(lambda x: re.sub(r'\s+', ' ', x).strip())
print("Text cleaning done.")
print()

# 4. Standardize genre and sentiment columns
df['genre'] = df['genre'].str.strip().str.title()
df['sentiment'] = df['sentiment'].str.strip().str.lower()

print("Unique genres:", df['genre'].unique().tolist())
print("Unique sentiments:", df['sentiment'].unique().tolist())
print()

# 5. Check data types
print("Data types:")
print(df.dtypes)
print()

# Save cleaned data
df.to_excel("cleaned_movie_reviews.xlsx", index=False)
print("Cleaned data saved to: cleaned_movie_reviews.xlsx")
print(f"Final shape: {df.shape[0]} rows x {df.shape[1]} columns")
