# Movie Success Prediction and Sentiment Study - Project Report

## 1. Introduction
This project aims to predict movie box office success and analyze audience sentiment based on a dataset of 10,000 movie reviews. The pipeline involves loading raw data, cleaning it to handle inconsistencies, performing sentiment analysis, and predicting gross earnings using machine learning.

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

### 3.2 Sentiment Analysis (Step 2)
We utilized the **VADER** (Valence Aware Dictionary and sEntiment Reasoner) tool to perform sentiment analysis on the cleaned review text. 
*   VADER calculated a compound score for each review ranging from -1 to +1.
*   Reviews were classified into three categories: Positive (score >= 0.05), Negative (score <= -0.05), and Neutral (scores in between).
*   The VADER classifications were then compared against the original sentiment labels to measure accuracy, achieving an approximate 70% match.

### 3.3 Prediction Model (Step 2)
A **Linear Regression** model was built to predict the `gross_earning` of a movie.
*   **Features Used**: `rating`, `budget`, and `vader_score`.
*   **Target Variable**: `gross_earning`.
*   The data was split into a training set (80%) and a testing set (20%).
*   The model's performance was evaluated using the Root Mean Squared Error (RMSE) and R-squared (R2) metrics.

### 3.4 Visualizations (Step 3)
To better understand the data, five key visual charts were generated:
1.  **Average Sentiment Score by Genre** (Bar Chart) - Showcased which genres are generally received most positively.
2.  **Predicted vs Actual Gross Earnings** (Scatter Plot) - Illustrated how close the model's predictions were to reality.
3.  **Sentiment Distribution** (Pie Chart) - Displayed the percentage of positive, negative, and neutral reviews.
4.  **Rating Distribution by Genre** (Box Plot) - Summarized how movie ratings spread across different genres.
5.  **Correlation Matrix** (Heatmap) - Showed relationships between numerical values like budget, rating, and gross earnings.

## 4. Results and Inferences (Step 4)

### Sentiment Findings
*   **Overall Sentiment**: The vast majority of the 10,000 reviews were positive (70%), indicating generally favorable audience reactions.
*   **Genre Trends**: The 'Romance' genre had the highest average positive sentiment, while 'Sci-Fi' received the lowest.
*   **Tool Accuracy**: VADER proved to be a reliable automated tool, closely matching human-labeled sentiments.

### Prediction Model Findings
*   The Linear Regression model produced a very low R2 score (close to 0). 
*   **Conclusion on Box Office Success**: The model demonstrated that `rating`, `budget`, and `review sentiment` alone are **not** sufficient to accurately predict how much money a movie will make. 
*   Movie success relies heavily on external factors not present in the dataset, such as marketing strategies, star power (famous cast members), release date, franchise popularity, and competition from other movies.

## 5. Conclusion
This project successfully demonstrated a complete data science pipeline, from data cleaning to machine learning. It highlighted that while automated sentiment analysis is quite effective at understanding audience reception, predicting financial success in the film industry requires a much broader set of data points beyond basic budgets and ratings.
