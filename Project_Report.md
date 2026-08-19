# Movie Success Prediction and Sentiment Study - Project Report

## 1. Introduction
This project aims to predict movie box office success and analyze audience sentiment based on a dataset of 10,000 movie reviews. The pipeline involves loading raw data, cleaning it to handle inconsistencies, performing advanced sentiment analysis, and predicting gross earnings using machine learning.

## 2. Dataset Overview
The dataset (`movie_reviews_10000_varied_titles.xlsx`) contains 10,000 records. Key features include:
*   **movie_title**: Name of the movie.
*   **genre**: The genre category (e.g., Action, Drama, Romance).
*   **rating**: Movie rating (scale of 5.0 to 9.5).
*   **budget**: Production budget in dollars.
*   **gross_earning**: Box office earnings.
*   **review_tweet**: A short text review by the audience.
*   **sentiment**: Original label of the sentiment (positive, neutral, negative).

## 3. Methodology

### 3.1 Data Cleaning (Step 1)
To prepare the data for analysis, several cleaning steps were performed:
*   **Missing Values and Duplicates**: The dataset was checked for null values and duplicate rows to ensure data integrity.
*   **Text Preprocessing**: The review text was converted to lowercase, extra spaces were stripped, and special characters were removed to provide clean input for sentiment analysis.
*   **Standardization**: Categorical columns like `genre` and `sentiment` were standardized (e.g., Title Case for genres, lowercase for sentiments) to prevent inconsistencies.

### 3.2 Sentiment Analysis using VADER (Step 2)
To understand audience reception beyond simple numerical ratings, Natural Language Processing (NLP) was used. Specifically, we utilized the **VADER** (Valence Aware Dictionary and sEntiment Reasoner) tool.

**What is VADER and Why Use It?**
VADER is a lexicon and rule-based sentiment analysis tool specifically attuned to sentiments expressed in social media and short texts (like tweets or movie reviews). 
*   **Lexicon-Based**: It relies on a dictionary that maps words to sentiment values (e.g., "excellent" is highly positive, "terrible" is highly negative).
*   **Context-Aware**: Unlike simple keyword counters, VADER understands the impact of punctuation (like exclamation marks "!!!"), capitalization (like "GREAT" vs "great"), and modifiers (like "extremely good" vs "marginally good"). It also understands negations (e.g., "not good").

**How it was applied:**
*   VADER analyzed each cleaned `review_tweet` and calculated a **compound score** ranging from -1 (most extreme negative) to +1 (most extreme positive).
*   Reviews were classified into discrete categories based on standard thresholds: Positive (score >= 0.05), Negative (score <= -0.05), and Neutral (scores between -0.05 and 0.05).
*   The VADER classifications were compared against the dataset's original human-labeled sentiments, achieving a ~70% match. This demonstrates VADER's strong capability in automating human subjective labeling.

### 3.3 Prediction Model (Step 2)
A **Linear Regression** model was built to predict the `gross_earning` of a movie.
*   **Features Used**: `rating`, `budget`, and the newly calculated `vader_score`.
*   **Target Variable**: `gross_earning`.
*   The data was split into a training set (80%) and a testing set (20%).
*   The model's performance was evaluated using the Root Mean Squared Error (RMSE) and R-squared (R2) metrics.

### 3.4 Visualizations (Step 3)
To better understand the data, five key visual charts were generated:
1.  **Average Sentiment Score by Genre** (Bar Chart) - Showcased which genres are generally received most positively based on VADER scoring.
2.  **Predicted vs Actual Gross Earnings** (Scatter Plot) - Illustrated how close the model's predictions were to reality.
3.  **Sentiment Distribution** (Pie Chart) - Displayed the percentage of positive, negative, and neutral reviews found by VADER.
4.  **Rating Distribution by Genre** (Box Plot) - Summarized how movie ratings spread across different genres.
5.  **Correlation Matrix** (Heatmap) - Showed relationships between numerical values like budget, rating, sentiment score, and gross earnings.

## 4. Results and Inferences (Step 4)

### Sentiment Analysis Findings
*   **Overall Sentiment**: The vast majority of the 10,000 reviews were categorized as positive (70%), indicating generally favorable audience reactions in this dataset.
*   **Genre Trends**: The 'Romance' genre had the highest average positive sentiment, while 'Sci-Fi' received the lowest. However, the overall variance between genres was small, indicating relatively uniform audience enthusiasm across movie types.
*   **Tool Accuracy**: VADER proved to be a highly effective automated tool for parsing audience text, scaling human-like judgment across 10,000 data points in seconds.

### Prediction Model Findings
*   The Linear Regression model produced a very low R2 score (close to 0). Consequently, the model's predictions formed a flat horizontal line, defaulting to predicting the mean average box office return for every movie regardless of input.
*   **Conclusion on Box Office Success**: The model empirically demonstrated that `rating`, `budget`, and `review sentiment` alone are **not** sufficient to accurately predict financial performance. 
*   Movie success relies heavily on complex, external features not present in this dataset, such as marketing strategies, star power, release date timing, franchise popularity, and competition from other movies.

## 5. Conclusion
This project successfully demonstrated a complete data science pipeline, integrating Natural Language Processing (VADER) with Machine Learning (Linear Regression). It proved that while NLP tools like VADER are highly effective for extracting qualitative insights from audience text, predicting hard financial success in the film industry requires a much broader, multi-dimensional set of data points beyond basic budgets and audience opinions.
