# Movie Success Prediction & Sentiment Study

## What is this project about?

This project analyzes 10,000 movie reviews to:
1. **Clean the data** - remove problems in the dataset before analysis
2. **Analyze sentiment** - use VADER to find if reviews are positive, negative, or neutral
3. **Predict box office earnings** - use Linear Regression to see if we can predict how much money a movie will make
4. **Visualize the results** - create charts and graphs
5. **Draw conclusions** - summarize what we learned

---

## How to run

Install required packages first:
```
pip install pandas matplotlib seaborn scikit-learn vaderSentiment openpyxl
```

Then run the scripts in order:
```
python 01_data_loading_and_cleaning.py
python 02_analysis.py
python 03_visualizations.py
python 04_inferences.py
```

---

## Files in this project

| File | What it does |
|------|-------------|
| `movie_reviews_10000_varied_titles.xlsx` | The raw dataset (10,000 reviews) |
| `01_data_loading_and_cleaning.py` | Loads and cleans the data |
| `02_analysis.py` | Runs sentiment analysis and builds prediction model |
| `03_visualizations.py` | Creates 5 charts/graphs |
| `04_inferences.py` | Prints conclusions and findings |
| `plots/` | Folder where all graphs are saved |

---

## Dataset columns

| Column | What it contains |
|--------|-----------------|
| movie_title | Name of the movie |
| genre | Genre (Action, Drama, Romance, etc.) |
| rating | Movie rating (5.0 to 9.5) |
| budget | How much the movie cost to make |
| gross_earning | How much the movie earned |
| review_tweet | The actual review text |
| sentiment | Original sentiment label (positive/neutral/negative) |

---

## Tools used

- Python
- Pandas (for data handling)
- Matplotlib & Seaborn (for graphs)
- Scikit-learn (for Linear Regression)
- VADER from vaderSentiment (for sentiment analysis)
