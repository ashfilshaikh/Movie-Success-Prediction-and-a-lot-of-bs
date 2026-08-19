# Step 2: Sentiment Analysis and Prediction Model
# This script performs VADER sentiment analysis and builds a prediction model

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from math import sqrt

# Load the cleaned data
print("Loading cleaned data...")
df = pd.read_excel("cleaned_movie_reviews.xlsx")
print(f"Loaded {len(df)} rows.")
print()

# --- VADER Sentiment Analysis ---

print("Running VADER sentiment analysis...")
analyzer = SentimentIntensityAnalyzer()

# Get sentiment score for each review
df['vader_score'] = df['review_tweet'].apply(
    lambda x: analyzer.polarity_scores(str(x))['compound']
)

# Classify sentiment based on score
def classify_sentiment(score):
    if score >= 0.05:
        return 'positive'
    elif score <= -0.05:
        return 'negative'
    else:
        return 'neutral'

df['vader_sentiment'] = df['vader_score'].apply(classify_sentiment)

# Show sentiment distribution
print("VADER Sentiment Distribution:")
print(df['vader_sentiment'].value_counts())
print()

# Compare VADER results with original labels
matches = (df['sentiment'] == df['vader_sentiment']).sum()
accuracy = matches / len(df) * 100
print(f"VADER vs Original Labels: {accuracy:.1f}% match")
print()

# --- Genre-wise Sentiment ---

print("Average sentiment score by genre:")
genre_avg = df.groupby('genre')['vader_score'].mean().sort_values(ascending=False)
print(genre_avg)
print()

# --- Linear Regression Model ---

print("Building prediction model...")

# Features and target
X = df[['rating', 'budget', 'vader_score']]
y = df['gross_earning']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate metrics
rmse = sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"RMSE: {rmse:,.2f}")
print(f"R2 Score: {r2:.4f}")
print()

# Show model coefficients
print("Model Coefficients:")
for feature, coef in zip(['rating', 'budget', 'vader_score'], model.coef_):
    print(f"  {feature}: {coef:.4f}")
print(f"  Intercept: {model.intercept_:.4f}")
print()

# Save prediction results for visualization
pred_df = pd.DataFrame({
    'actual_gross': y_test.values,
    'predicted_gross': y_pred
})
pred_df.to_excel("prediction_results.xlsx", index=False)

# Save the analyzed data with vader columns
df.to_excel("analyzed_movie_reviews.xlsx", index=False)
print("Analysis complete! Files saved.")
