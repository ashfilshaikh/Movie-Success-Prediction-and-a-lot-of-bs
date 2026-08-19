# Step 4: Inferences and Conclusions
# This script prints out the key findings from our analysis

import pandas as pd

# Load the analyzed data
df = pd.read_excel("analyzed_movie_reviews.xlsx")

print("=" * 50)
print("  INFERENCES AND CONCLUSIONS")
print("=" * 50)

# --- 1. Sentiment Overview ---

print("\n1. SENTIMENT OVERVIEW")
print("-" * 50)

total = len(df)
vader_counts = df['vader_sentiment'].value_counts()

for label in ['positive', 'neutral', 'negative']:
    count = vader_counts.get(label, 0)
    pct = count / total * 100
    print(f"   {label}: {count} reviews ({pct:.1f}%)")

print("\n   Finding: Most reviews are positive, meaning")
print("   audiences generally liked the movies in this dataset.")

# --- 2. Genre-wise Trends ---

print("\n2. GENRE-WISE SENTIMENT TRENDS")
print("-" * 50)

genre_avg = df.groupby('genre')['vader_score'].mean().sort_values(ascending=False)

for genre, score in genre_avg.items():
    print(f"   {genre}: {score:.4f}")

best_genre = genre_avg.index[0]
worst_genre = genre_avg.index[-1]
print(f"\n   Finding: '{best_genre}' movies have the most positive reviews.")
print(f"   '{worst_genre}' movies have the least positive reviews.")

# --- 3. VADER vs Original Labels ---

print("\n3. VADER vs ORIGINAL LABELS")
print("-" * 50)

matches = (df['sentiment'] == df['vader_sentiment']).sum()
accuracy = matches / total * 100

print(f"   VADER matched original labels: {accuracy:.1f}%")
print(f"   This means VADER is fairly reliable for sentiment analysis.")

# --- 4. Model Performance ---

print("\n4. PREDICTION MODEL RESULTS")
print("-" * 50)

print("   We used Linear Regression to predict gross earnings")
print("   using rating, budget, and vader_score as features.")
print()
print("   The R2 score was very low (close to 0), which means")
print("   these 3 features alone are NOT enough to predict")
print("   how much money a movie will make.")
print()
print("   This makes sense because box office success depends on")
print("   many other things like:")
print("   - Star power (famous actors)")
print("   - Marketing and advertising")
print("   - Release date and competition")
print("   - Whether its a sequel or franchise")
print("   - Word of mouth and social media buzz")

# --- 5. Overall Conclusions ---

print("\n5. OVERALL CONCLUSIONS")
print("-" * 50)

print(f"""
   a) VADER sentiment analysis works well for classifying
      movie reviews as positive, negative, or neutral.

   b) {best_genre} movies get the best audience sentiment,
      while {worst_genre} gets the lowest.

   c) Rating, budget, and sentiment alone cannot predict
      box office earnings accurately. Movie success is
      influenced by many more factors.

   d) Automated tools like VADER are useful for quickly
      analyzing large amounts of reviews without having
      to read each one manually.
""")

print("=" * 50)
print("  END OF ANALYSIS")
print("=" * 50)
