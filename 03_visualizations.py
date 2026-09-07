# Step 3: Visualizations
# This script creates charts and graphs from the analyzed data

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load analyzed data
df = pd.read_excel("analyzed_movie_reviews.xlsx")
print(f"Loaded {len(df)} rows.")

# Create folder to save plots
os.makedirs("plots", exist_ok=True)

# --- Plot 1: Average Sentiment by Genre (Bar Chart) ---

genre_sentiment = df.groupby('genre')['vader_score'].mean().sort_values()

plt.figure(figsize=(10, 6))
sns.barplot(x=genre_sentiment.index, y=genre_sentiment.values, hue=genre_sentiment.index, palette='coolwarm', legend=False)
plt.title("Average Sentiment Score by Genre")
plt.ylabel("Average VADER Score")
plt.xlabel("Genre")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("plots/01_sentiment_by_genre.png")
plt.close()
print("Saved: plots/01_sentiment_by_genre.png")

# --- Plot 2: Predicted vs Actual Gross Earnings (Scatter Plot) ---

pred_df = pd.read_excel("prediction_results.xlsx")

plt.figure(figsize=(8, 6))
plt.scatter(pred_df['actual_gross'], pred_df['predicted_gross'], alpha=0.5)
plt.plot([pred_df['actual_gross'].min(), pred_df['actual_gross'].max()],
         [pred_df['actual_gross'].min(), pred_df['actual_gross'].max()],
         'r--', label='Perfect Prediction')
plt.xlabel("Actual Gross Earning")
plt.ylabel("Predicted Gross Earning")
plt.title("Predicted vs Actual Box Office Revenue")
plt.legend()
plt.tight_layout()
plt.savefig("plots/02_predicted_vs_actual.png")
plt.close()
print("Saved: plots/02_predicted_vs_actual.png")

# --- Plot 3: Sentiment Distribution (Pie Chart) ---

sentiment_counts = df['vader_sentiment'].value_counts()

plt.figure(figsize=(8, 6))
plt.pie(sentiment_counts.values,
        labels=sentiment_counts.index,
        autopct='%1.1f%%',
        colors=['#2ecc71', '#e74c3c', '#f39c12'])
plt.title("VADER Sentiment Distribution")
plt.tight_layout()
plt.savefig("plots/03_sentiment_distribution.png")
plt.close()
print("Saved: plots/03_sentiment_distribution.png")

# --- Plot 4: Rating Distribution by Genre (Box Plot) ---

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='genre', y='rating', hue='genre', palette='Set2', legend=False)
plt.title("Movie Rating Distribution by Genre")
plt.ylabel("Rating")
plt.xlabel("Genre")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("plots/04_rating_by_genre.png")
plt.close()
print("Saved: plots/04_rating_by_genre.png")

# --- Plot 5: Correlation Heatmap ---

plt.figure(figsize=(8, 6))
corr = df[['rating', 'budget', 'gross_earning', 'vader_score']].corr()
sns.heatmap(corr, annot=True, cmap='RdYlGn', fmt='.3f')
plt.title("Correlation Matrix")
plt.tight_layout()
plt.savefig("plots/05_correlation_heatmap.png")
plt.close()
print("Saved: plots/05_correlation_heatmap.png")

# --- Plot 6: Budget vs Gross Earning (Scatter Plot) ---

plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='budget', y='gross_earning', alpha=0.6, color='purple')
plt.title("Budget vs Gross Earning")
plt.xlabel("Budget")
plt.ylabel("Gross Earning")
plt.tight_layout()
plt.savefig("plots/06_budget_vs_gross.png")
plt.close()
print("Saved: plots/06_budget_vs_gross.png")

# --- Plot 7: Number of Movies by Genre (Count Plot) ---

plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='genre', order=df['genre'].value_counts().index, palette='viridis', hue='genre', legend=False)
plt.title("Number of Movies by Genre")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("plots/07_movies_per_genre.png")
plt.close()
print("Saved: plots/07_movies_per_genre.png")

# --- Plot 8: Distribution of VADER Scores (Histogram) ---

plt.figure(figsize=(8, 6))
sns.histplot(df['vader_score'], bins=30, kde=True, color='teal')
plt.title("Distribution of VADER Sentiment Scores")
plt.xlabel("VADER Score")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("plots/08_vader_score_distribution.png")
plt.close()
print("Saved: plots/08_vader_score_distribution.png")

# --- Plot 9: Rating vs Gross Earning (Scatter Plot) ---

plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='rating', y='gross_earning', alpha=0.5, color='orange')
plt.title("Rating vs Gross Earning")
plt.xlabel("Rating")
plt.ylabel("Gross Earning")
plt.tight_layout()
plt.savefig("plots/09_rating_vs_gross.png")
plt.close()
print("Saved: plots/09_rating_vs_gross.png")

print("\nAll visualizations saved in plots/ folder.")
