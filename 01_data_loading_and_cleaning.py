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

# 1. Check and handle missing values
print("Checking for missing values...")
print(df.isnull().sum())
print()

missing = df.isnull().sum().sum()
if missing > 0:
    print(f"Found {missing} missing values. Imputing numeric columns with median and dropping rest...")
    # Impute numeric columns with median
    numeric_cols = df.select_dtypes(include=['number']).columns
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())
    
    # Drop rows if they still have missing values (e.g., categorical/text columns)
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

# 3. Handle invalid numerical values
print("Handling numerical anomalies...")
if 'budget' in df.columns:
    df['budget'] = df['budget'].abs() # Ensure budget is positive
if 'gross_earning' in df.columns:
    df['gross_earning'] = df['gross_earning'].abs() # Ensure gross earning is positive
print()

# 4. Clean the review text and other strings
print("Cleaning text columns...")
if 'movie_title' in df.columns:
    df['movie_title'] = df['movie_title'].astype(str).str.strip().str.title()

df['review_tweet'] = df['review_tweet'].astype(str).str.strip()
df['review_tweet'] = df['review_tweet'].str.lower()
# Remove URLs
df['review_tweet'] = df['review_tweet'].apply(lambda x: re.sub(r'http\S+|www\.\S+', '', x))
# Remove HTML tags
df['review_tweet'] = df['review_tweet'].apply(lambda x: re.sub(r'<.*?>', '', x))
# Remove numbers
df['review_tweet'] = df['review_tweet'].apply(lambda x: re.sub(r'\d+', '', x))
# Remove special characters
df['review_tweet'] = df['review_tweet'].apply(lambda x: re.sub(r'[^a-z\s.,!?\'-]', '', x))
# Remove extra spaces
df['review_tweet'] = df['review_tweet'].apply(lambda x: re.sub(r'\s+', ' ', x).strip())
print("Text cleaning done.")
print()

# 5. Standardize genre and sentiment columns
df['genre'] = df['genre'].str.strip().str.title()
df['sentiment'] = df['sentiment'].str.strip().str.lower()

print("Unique genres:", df['genre'].unique().tolist())
print("Unique sentiments:", df['sentiment'].unique().tolist())
print()

# 6. Check data types
print("Data types:")
print(df.dtypes)
print()

# Save cleaned data
df.to_excel("cleaned_movie_reviews.xlsx", index=False)
print("Cleaned data saved to: cleaned_movie_reviews.xlsx")
print(f"Final shape: {df.shape[0]} rows x {df.shape[1]} columns")
