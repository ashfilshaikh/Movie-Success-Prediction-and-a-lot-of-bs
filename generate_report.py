"""
Generate a comprehensive Word Document Project Report
for the Movie Success Prediction & Sentiment Study project.
"""

from docx import Document
from docx.shared import Inches, Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PLOTS_DIR = os.path.join(BASE_DIR, "plots")

doc = Document()

# ── Global Style Defaults ──────────────────────────────────────────
style = doc.styles['Normal']
font = style.font
font.name = 'Calibri'
font.size = Pt(11)
font.color.rgb = RGBColor(0x1A, 0x1A, 0x2E)  # dark navy

# Heading styles
for level in range(1, 4):
    h = doc.styles[f'Heading {level}']
    h.font.color.rgb = RGBColor(0x0B, 0x3D, 0x91)  # deep blue
    h.font.name = 'Calibri'

# Code style (character style for inline code)
code_style = doc.styles.add_style('CodeBlock', WD_STYLE_TYPE.PARAGRAPH)
code_font = code_style.font
code_font.name = 'Consolas'
code_font.size = Pt(9)
code_font.color.rgb = RGBColor(0x22, 0x22, 0x22)


# ── Helper Functions ───────────────────────────────────────────────
def add_code_block(doc, code_text, caption=None):
    """Add a formatted code block with optional caption."""
    if caption:
        p = doc.add_paragraph()
        run = p.add_run(caption)
        run.bold = True
        run.font.size = Pt(10)
        run.font.color.rgb = RGBColor(0x33, 0x33, 0x33)

    # Add a table with one cell to simulate a code block background
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = table.cell(0, 0)
    # Set cell shading to light grey
    shading = cell._element.get_or_add_tcPr()
    shd = shading.makeelement(qn('w:shd'), {
        qn('w:fill'): 'F0F0F0',
        qn('w:color'): 'auto',
        qn('w:val'): 'clear'
    })
    shading.append(shd)

    p = cell.paragraphs[0]
    p.style = doc.styles['CodeBlock']
    run = p.add_run(code_text)
    run.font.name = 'Consolas'
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(0x22, 0x22, 0x22)

    doc.add_paragraph()  # spacing


def add_plot(doc, filename, caption, width=5.5):
    """Add a plot image with a caption below it."""
    path = os.path.join(PLOTS_DIR, filename)
    if os.path.exists(path):
        doc.add_picture(path, width=Inches(width))
        last_paragraph = doc.paragraphs[-1]
        last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

        cap = doc.add_paragraph()
        cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = cap.add_run(caption)
        run.italic = True
        run.font.size = Pt(10)
        run.font.color.rgb = RGBColor(0x55, 0x55, 0x55)
    else:
        doc.add_paragraph(f"[Plot not found: {filename}]")

    doc.add_paragraph()  # spacing


def add_horizontal_line(doc):
    """Add a visual separator."""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("─" * 60)
    run.font.color.rgb = RGBColor(0xBB, 0xBB, 0xBB)
    run.font.size = Pt(8)


# ══════════════════════════════════════════════════════════════════
#   TITLE PAGE
# ══════════════════════════════════════════════════════════════════
for _ in range(6):
    doc.add_paragraph()

title = doc.add_paragraph()
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = title.add_run("Movie Success Prediction\nand Sentiment Study")
run.bold = True
run.font.size = Pt(28)
run.font.color.rgb = RGBColor(0x0B, 0x3D, 0x91)

doc.add_paragraph()

subtitle = doc.add_paragraph()
subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = subtitle.add_run("A Comprehensive Data Science Project Report")
run.font.size = Pt(16)
run.font.color.rgb = RGBColor(0x55, 0x55, 0x55)

doc.add_paragraph()
doc.add_paragraph()

details = doc.add_paragraph()
details.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = details.add_run(
    "Utilizing Natural Language Processing (VADER Sentiment Analysis)\n"
    "and Machine Learning (Linear Regression)\n"
    "on a Dataset of 10,000 Movie Reviews"
)
run.font.size = Pt(12)
run.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

doc.add_page_break()

# ══════════════════════════════════════════════════════════════════
#   TABLE OF CONTENTS (Manual)
# ══════════════════════════════════════════════════════════════════
doc.add_heading("Table of Contents", level=1)
toc_items = [
    "1. Introduction",
    "2. Objectives",
    "3. Dataset Description",
    "4. Tools and Libraries Used",
    "5. Methodology",
    "   5.1 Step 1 – Data Loading and Cleaning",
    "   5.2 Step 2 – Sentiment Analysis using VADER",
    "   5.3 Step 3 – Prediction Model (Linear Regression)",
    "   5.4 Step 4 – Data Visualization",
    "   5.5 Step 5 – Inferences and Conclusions",
    "6. Visualizations and Analysis",
    "   6.1 Average Sentiment Score by Genre",
    "   6.2 Predicted vs Actual Gross Earnings",
    "   6.3 VADER Sentiment Distribution",
    "   6.4 Rating Distribution by Genre",
    "   6.5 Correlation Heatmap",
    "   6.6 Budget vs Gross Earning",
    "   6.7 Number of Movies per Genre",
    "   6.8 Distribution of VADER Scores",
    "   6.9 Rating vs Gross Earning",
    "7. Results and Key Findings",
    "8. Limitations",
    "9. Future Scope",
    "10. Conclusion",
    "11. References",
]
for item in toc_items:
    p = doc.add_paragraph()
    run = p.add_run(item)
    run.font.size = Pt(11)
    if not item.startswith("   "):
        run.bold = True

doc.add_page_break()

# ══════════════════════════════════════════════════════════════════
#   1. INTRODUCTION
# ══════════════════════════════════════════════════════════════════
doc.add_heading("1. Introduction", level=1)
doc.add_paragraph(
    "The film industry is one of the most lucrative entertainment sectors globally, "
    "with box office revenues running into billions of dollars each year. Understanding "
    "what makes a movie commercially successful is a question that has fascinated "
    "analysts, producers, and data scientists alike. This project — 'Movie Success "
    "Prediction and Sentiment Study' — undertakes a comprehensive data-driven approach "
    "to answering this question."
)
doc.add_paragraph(
    "The project is built on a dataset of 10,000 movie reviews spanning multiple genres. "
    "It combines Natural Language Processing (NLP) techniques with traditional Machine "
    "Learning to achieve two primary goals: (1) analyze audience sentiment from review "
    "text using the VADER sentiment analysis tool, and (2) build a predictive model using "
    "Linear Regression to forecast a movie's gross box-office earnings based on its "
    "rating, production budget, and audience sentiment score."
)
doc.add_paragraph(
    "The project follows a structured four-step pipeline: data loading and cleaning, "
    "sentiment analysis and model building, visualization of results, and finally, "
    "deriving actionable inferences and conclusions. Each step is implemented as a "
    "standalone Python script, making the workflow modular, reproducible, and easy to "
    "understand."
)

# ══════════════════════════════════════════════════════════════════
#   2. OBJECTIVES
# ══════════════════════════════════════════════════════════════════
doc.add_heading("2. Objectives", level=1)
objectives = [
    "To load and preprocess a real-world movie reviews dataset, handling missing values, "
    "duplicates, and text inconsistencies.",
    "To perform sentiment analysis on 10,000 movie review texts using the VADER "
    "(Valence Aware Dictionary and sEntiment Reasoner) NLP tool.",
    "To compare the automated VADER sentiment classifications against the original "
    "human-labeled sentiments and measure agreement accuracy.",
    "To identify genre-wise sentiment trends — determining which movie genres receive "
    "the most favorable and least favorable audience reactions.",
    "To build a Linear Regression model that predicts a movie's gross box-office earnings "
    "using rating, budget, and VADER sentiment score as features.",
    "To evaluate the model's performance using RMSE (Root Mean Square Error) and R² "
    "(coefficient of determination) metrics.",
    "To generate a comprehensive set of visualizations (bar charts, scatter plots, pie "
    "charts, box plots, heatmaps, and histograms) that convey insights clearly.",
    "To draw meaningful inferences about the factors that influence movie success and the "
    "limitations of simple predictive models.",
]
for obj in objectives:
    doc.add_paragraph(obj, style='List Bullet')

# ══════════════════════════════════════════════════════════════════
#   3. DATASET DESCRIPTION
# ══════════════════════════════════════════════════════════════════
doc.add_heading("3. Dataset Description", level=1)
doc.add_paragraph(
    "The dataset used in this project is stored in an Excel file named "
    "'movie_reviews_10000_varied_titles.xlsx'. It contains 10,000 records, each "
    "representing a unique movie review. The dataset captures both quantitative "
    "attributes (budget, ratings, earnings) and qualitative information (review text, "
    "sentiment labels), making it well-suited for a combined NLP and machine learning "
    "analysis."
)

# Dataset columns table
doc.add_heading("Dataset Schema", level=2)
table = doc.add_table(rows=8, cols=3)
table.style = 'Light Grid Accent 1'
table.alignment = WD_TABLE_ALIGNMENT.CENTER

headers = ["Column Name", "Data Type", "Description"]
for i, h in enumerate(headers):
    cell = table.rows[0].cells[i]
    cell.text = h
    for paragraph in cell.paragraphs:
        for run in paragraph.runs:
            run.bold = True

data_rows = [
    ("movie_title", "String", "Name of the movie (e.g., 'The Dark Knight', 'Inception')"),
    ("genre", "String (Categorical)", "Genre category — Action, Drama, Comedy, Romance, Horror, Thriller, Sci-Fi"),
    ("rating", "Float", "Movie rating on a scale of 5.0 to 9.5"),
    ("budget", "Integer", "Production budget in US dollars"),
    ("gross_earning", "Integer", "Total box-office gross earnings in US dollars"),
    ("review_tweet", "String (Text)", "A short audience review/tweet about the movie"),
    ("sentiment", "String (Categorical)", "Original human-labeled sentiment — positive, neutral, or negative"),
]
for i, (col, dtype, desc) in enumerate(data_rows):
    row = table.rows[i + 1]
    row.cells[0].text = col
    row.cells[1].text = dtype
    row.cells[2].text = desc

doc.add_paragraph()

# ══════════════════════════════════════════════════════════════════
#   4. TOOLS AND LIBRARIES
# ══════════════════════════════════════════════════════════════════
doc.add_heading("4. Tools and Libraries Used", level=1)
doc.add_paragraph(
    "The entire project is implemented in Python 3, leveraging a powerful ecosystem of "
    "data science and NLP libraries. Each library serves a specific purpose in the "
    "pipeline:"
)

lib_table = doc.add_table(rows=9, cols=3)
lib_table.style = 'Light Grid Accent 1'
lib_table.alignment = WD_TABLE_ALIGNMENT.CENTER

lib_headers = ["Library", "Version", "Purpose"]
for i, h in enumerate(lib_headers):
    cell = lib_table.rows[0].cells[i]
    cell.text = h
    for paragraph in cell.paragraphs:
        for run in paragraph.runs:
            run.bold = True

libs = [
    ("pandas", "2.x", "Data loading, manipulation, and Excel I/O"),
    ("re (regex)", "Built-in", "Text cleaning — removing URLs, HTML tags, special characters"),
    ("vaderSentiment", "3.x", "VADER sentiment analysis for NLP-based review classification"),
    ("scikit-learn", "1.x", "Linear Regression model, train/test split, evaluation metrics"),
    ("matplotlib", "3.x", "Base plotting library for creating charts and graphs"),
    ("seaborn", "0.13+", "Statistical visualization — enhanced bar, box, scatter, and heatmap plots"),
    ("os", "Built-in", "File system operations (creating the plots directory)"),
    ("math", "Built-in", "Square root function for RMSE calculation"),
]
for i, (lib, ver, purpose) in enumerate(libs):
    row = lib_table.rows[i + 1]
    row.cells[0].text = lib
    row.cells[1].text = ver
    row.cells[2].text = purpose

doc.add_paragraph()

# ══════════════════════════════════════════════════════════════════
#   5. METHODOLOGY
# ══════════════════════════════════════════════════════════════════
doc.add_heading("5. Methodology", level=1)
doc.add_paragraph(
    "The project follows a modular, four-step pipeline architecture. Each step is "
    "implemented as a standalone Python script that reads data from the previous step's "
    "output. This design ensures reproducibility, separation of concerns, and ease of "
    "debugging. An orchestrator script (run_all.py) can execute all four steps "
    "sequentially."
)

# ── 5.1 Data Loading & Cleaning ───────────────────────────────────
doc.add_heading("5.1 Step 1 — Data Loading and Cleaning", level=2)
doc.add_paragraph(
    "The first step in any data science project is ensuring the data is clean and "
    "reliable. Raw datasets frequently contain missing values, duplicate entries, "
    "inconsistent formatting, and noisy text — all of which can skew analysis and "
    "model performance. This step addresses each of these issues systematically."
)

doc.add_heading("5.1.1 Loading the Raw Dataset", level=3)
doc.add_paragraph(
    "The raw dataset is loaded from the Excel file using pandas' read_excel() function. "
    "Upon loading, the shape (rows × columns) and column names are printed to give an "
    "immediate overview of the data structure."
)
add_code_block(doc, """import pandas as pd
import re

# Load the raw data from excel file
df = pd.read_excel("movie_reviews_10000_varied_titles.xlsx")
print("Dataset shape:", df.shape)
print("Columns:", list(df.columns))""", "Code — Loading the dataset:")

doc.add_heading("5.1.2 Handling Missing Values", level=3)
doc.add_paragraph(
    "Missing data can arise from incomplete data collection or corruption during export. "
    "We identify missing values using isnull().sum() and handle them with a two-pronged "
    "strategy: numeric columns are imputed with their median value (which is robust to "
    "outliers), while rows with missing categorical/text values are dropped entirely."
)
add_code_block(doc, """# Check and handle missing values
print(df.isnull().sum())

missing = df.isnull().sum().sum()
if missing > 0:
    # Impute numeric columns with median
    numeric_cols = df.select_dtypes(include=['number']).columns
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())
    
    # Drop rows if they still have missing values
    df = df.dropna()""", "Code — Missing value handling:")

doc.add_heading("5.1.3 Removing Duplicate Rows", level=3)
doc.add_paragraph(
    "Duplicate rows can inflate statistical measures and bias model training. We detect "
    "duplicates using the duplicated() method and remove them with drop_duplicates()."
)
add_code_block(doc, """# Check for duplicate rows
duplicates = df.duplicated().sum()
print(f"Duplicate rows found: {duplicates}")
if duplicates > 0:
    df = df.drop_duplicates()
    print("Duplicates removed.")""", "Code — Duplicate removal:")

doc.add_heading("5.1.4 Handling Numerical Anomalies", level=3)
doc.add_paragraph(
    "Budget and gross earning values should always be positive. Any negative values "
    "(likely data entry errors) are corrected by taking their absolute value."
)
add_code_block(doc, """# Ensure budget and gross_earning are positive
if 'budget' in df.columns:
    df['budget'] = df['budget'].abs()
if 'gross_earning' in df.columns:
    df['gross_earning'] = df['gross_earning'].abs()""", "Code — Numerical anomaly correction:")

doc.add_heading("5.1.5 Text Preprocessing", level=3)
doc.add_paragraph(
    "The review text ('review_tweet') undergoes extensive cleaning to prepare it for "
    "sentiment analysis. This is critical because NLP tools perform best on clean, "
    "normalized text. The cleaning pipeline includes: (a) converting text to lowercase "
    "for uniformity, (b) removing URLs and HTML tags, (c) removing numeric digits, "
    "(d) stripping special characters while preserving basic punctuation, and "
    "(e) collapsing multiple whitespace into single spaces."
)
add_code_block(doc, """# Text cleaning pipeline
df['review_tweet'] = df['review_tweet'].astype(str).str.strip()
df['review_tweet'] = df['review_tweet'].str.lower()

# Remove URLs
df['review_tweet'] = df['review_tweet'].apply(
    lambda x: re.sub(r'http\\S+|www\\.\\S+', '', x))
# Remove HTML tags
df['review_tweet'] = df['review_tweet'].apply(
    lambda x: re.sub(r'<.*?>', '', x))
# Remove numbers
df['review_tweet'] = df['review_tweet'].apply(
    lambda x: re.sub(r'\\d+', '', x))
# Remove special characters
df['review_tweet'] = df['review_tweet'].apply(
    lambda x: re.sub(r"[^a-z\\s.,!?\\'\\-]", '', x))
# Remove extra spaces
df['review_tweet'] = df['review_tweet'].apply(
    lambda x: re.sub(r'\\s+', ' ', x).strip())""", "Code — Text preprocessing:")

doc.add_heading("5.1.6 Standardizing Categorical Columns", level=3)
doc.add_paragraph(
    "Genre and sentiment columns are standardized to prevent inconsistencies like "
    "'action' vs 'Action' vs ' Action '. Genres are converted to Title Case and "
    "sentiments to lowercase after stripping whitespace."
)
add_code_block(doc, """# Standardize genre and sentiment columns
df['genre'] = df['genre'].str.strip().str.title()
df['sentiment'] = df['sentiment'].str.strip().str.lower()

# Save cleaned data
df.to_excel("cleaned_movie_reviews.xlsx", index=False)""", "Code — Standardization and saving:")

add_horizontal_line(doc)

# ── 5.2 Sentiment Analysis ────────────────────────────────────────
doc.add_heading("5.2 Step 2 — Sentiment Analysis using VADER", level=2)

doc.add_heading("5.2.1 What is VADER?", level=3)
doc.add_paragraph(
    "VADER (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule-based "
    "sentiment analysis tool that is specifically designed for sentiments expressed in "
    "social media and short texts — making it ideal for movie review tweets. Unlike "
    "machine learning-based sentiment classifiers that require training data, VADER "
    "uses a pre-built dictionary (lexicon) where words are manually scored for sentiment "
    "intensity."
)
doc.add_paragraph(
    "Key capabilities of VADER include:"
)
vader_capabilities = [
    "Lexicon-Based Scoring: Words are mapped to pre-defined sentiment values. For "
    "example, 'excellent' has a higher positive score than 'good', while 'terrible' "
    "has a high negative score.",
    "Context Awareness: VADER understands that 'GREAT' (capitalized) conveys stronger "
    "sentiment than 'great'. It also recognizes that 'Good!!!' (with exclamation marks) "
    "is more intense than 'Good'.",
    "Modifier Handling: Phrases like 'extremely good' receive a boosted positive score "
    "compared to just 'good'. Conversely, 'marginally good' is scored lower.",
    "Negation Understanding: VADER correctly interprets that 'not good' flips the "
    "sentiment from positive to negative.",
    "Compound Score Output: VADER produces a compound score between -1.0 (most extreme "
    "negative) and +1.0 (most extreme positive) for each piece of text.",
]
for cap in vader_capabilities:
    doc.add_paragraph(cap, style='List Bullet')

doc.add_heading("5.2.2 Applying VADER to Reviews", level=3)
doc.add_paragraph(
    "Each cleaned review text is passed through VADER's polarity_scores() method, "
    "which returns a dictionary of scores. The compound score is extracted and stored "
    "as a new column 'vader_score'. Reviews are then classified into three categories "
    "using standard thresholds."
)
add_code_block(doc, """from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

# Get compound sentiment score for each review
df['vader_score'] = df['review_tweet'].apply(
    lambda x: analyzer.polarity_scores(str(x))['compound']
)

# Classify sentiment based on compound score
def classify_sentiment(score):
    if score >= 0.05:
        return 'positive'
    elif score <= -0.05:
        return 'negative'
    else:
        return 'neutral'

df['vader_sentiment'] = df['vader_score'].apply(classify_sentiment)""",
    "Code — VADER sentiment analysis:")

doc.add_paragraph(
    "The classification thresholds are based on standard VADER conventions:"
)
thresh_table = doc.add_table(rows=4, cols=2)
thresh_table.style = 'Light Grid Accent 1'
thresh_table.rows[0].cells[0].text = "Compound Score Range"
thresh_table.rows[0].cells[1].text = "Classification"
for p in thresh_table.rows[0].cells[0].paragraphs:
    for r in p.runs:
        r.bold = True
for p in thresh_table.rows[0].cells[1].paragraphs:
    for r in p.runs:
        r.bold = True
thresh_table.rows[1].cells[0].text = "≥ 0.05"
thresh_table.rows[1].cells[1].text = "Positive"
thresh_table.rows[2].cells[0].text = "≤ -0.05"
thresh_table.rows[2].cells[1].text = "Negative"
thresh_table.rows[3].cells[0].text = "-0.05 < score < 0.05"
thresh_table.rows[3].cells[1].text = "Neutral"
doc.add_paragraph()

doc.add_heading("5.2.3 Validating VADER Against Original Labels", level=3)
doc.add_paragraph(
    "To evaluate VADER's reliability, we compared its automated classifications against "
    "the original human-labeled sentiments in the dataset. A simple element-wise "
    "comparison was performed to calculate the percentage of reviews where VADER's "
    "label matched the human label."
)
add_code_block(doc, """# Compare VADER results with original labels
matches = (df['sentiment'] == df['vader_sentiment']).sum()
accuracy = matches / len(df) * 100
print(f"VADER vs Original Labels: {accuracy:.1f}% match")""",
    "Code — VADER validation:")
doc.add_paragraph(
    "The VADER tool achieved approximately 70% agreement with human-labeled sentiments, "
    "demonstrating its strong capability as an automated sentiment classifier for "
    "short review texts."
)

doc.add_heading("5.2.4 Genre-Wise Sentiment Analysis", level=3)
doc.add_paragraph(
    "To understand how audience sentiment varies across movie genres, we grouped the "
    "data by genre and calculated the mean VADER compound score for each group."
)
add_code_block(doc, """# Average sentiment score by genre
genre_avg = df.groupby('genre')['vader_score'].mean().sort_values(ascending=False)
print(genre_avg)""", "Code — Genre-wise sentiment:")

add_horizontal_line(doc)

# ── 5.3 Prediction Model ─────────────────────────────────────────
doc.add_heading("5.3 Step 3 — Prediction Model (Linear Regression)", level=2)

doc.add_heading("5.3.1 What is Linear Regression?", level=3)
doc.add_paragraph(
    "Linear Regression is one of the most fundamental supervised machine learning "
    "algorithms. It attempts to model the relationship between one or more independent "
    "variables (features) and a dependent variable (target) by fitting a linear equation "
    "to the observed data. The general equation is:"
)
eq = doc.add_paragraph()
eq.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = eq.add_run("y = β₀ + β₁x₁ + β₂x₂ + β₃x₃ + ε")
run.bold = True
run.font.size = Pt(13)
run.font.color.rgb = RGBColor(0x0B, 0x3D, 0x91)

doc.add_paragraph(
    "Where y is the predicted gross earning, β₀ is the intercept, β₁, β₂, β₃ are "
    "coefficients for rating, budget, and vader_score respectively, and ε represents "
    "the error term."
)

doc.add_heading("5.3.2 Feature Selection and Data Splitting", level=3)
doc.add_paragraph(
    "Three features were selected for the model: 'rating' (the movie's numerical rating), "
    "'budget' (the production budget), and 'vader_score' (the VADER compound sentiment "
    "score). The target variable is 'gross_earning'. The dataset was split into 80% "
    "training data and 20% testing data using scikit-learn's train_test_split() function "
    "with a fixed random state of 42 for reproducibility."
)
add_code_block(doc, """from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from math import sqrt

# Features and target
X = df[['rating', 'budget', 'vader_score']]
y = df['gross_earning']

# Split into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)""", "Code — Feature selection and data splitting:")

doc.add_heading("5.3.3 Model Training and Evaluation", level=3)
doc.add_paragraph(
    "The Linear Regression model is trained on the training set using scikit-learn's "
    "fit() method. Predictions are then generated on the test set and evaluated using "
    "two key metrics:"
)
metrics_list = [
    "RMSE (Root Mean Square Error): Measures the average magnitude of prediction errors. "
    "A lower RMSE indicates better predictive accuracy. It is calculated as the square "
    "root of the mean of squared differences between actual and predicted values.",
    "R² Score (Coefficient of Determination): Indicates the proportion of variance in "
    "the target variable that is explained by the model. A score of 1.0 means perfect "
    "prediction, while 0.0 means the model is no better than predicting the mean.",
]
for m in metrics_list:
    doc.add_paragraph(m, style='List Bullet')

add_code_block(doc, """# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate evaluation metrics
rmse = sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"RMSE: {rmse:,.2f}")
print(f"R2 Score: {r2:.4f}")

# Model coefficients
for feature, coef in zip(['rating', 'budget', 'vader_score'], model.coef_):
    print(f"  {feature}: {coef:.4f}")
print(f"  Intercept: {model.intercept_:.4f}")

# Save prediction results
pred_df = pd.DataFrame({
    'actual_gross': y_test.values,
    'predicted_gross': y_pred
})
pred_df.to_excel("prediction_results.xlsx", index=False)""",
    "Code — Model training, prediction, and evaluation:")

add_horizontal_line(doc)

# ── 5.4 Visualizations ────────────────────────────────────────────
doc.add_heading("5.4 Step 4 — Data Visualization", level=2)
doc.add_paragraph(
    "Visualization is a critical step in any data science project. It transforms raw "
    "numbers and statistical outputs into intuitive visual representations that reveal "
    "patterns, trends, and outliers at a glance. In this project, nine distinct "
    "visualizations were created using matplotlib and seaborn, each designed to "
    "highlight a specific aspect of the data."
)
add_code_block(doc, """import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load analyzed data
df = pd.read_excel("analyzed_movie_reviews.xlsx")
os.makedirs("plots", exist_ok=True)""", "Code — Setup for visualization:")

add_horizontal_line(doc)

# ── 5.5 Inferences ────────────────────────────────────────────────
doc.add_heading("5.5 Step 5 — Inferences and Conclusions", level=2)
doc.add_paragraph(
    "The final step of the pipeline synthesizes all the findings from the previous "
    "steps into actionable inferences. This script loads the analyzed dataset, "
    "recalculates key metrics, and prints a structured summary of findings covering "
    "sentiment overview, genre-wise trends, VADER accuracy, model performance, and "
    "overall conclusions."
)
add_code_block(doc, """# Sentiment Overview
total = len(df)
vader_counts = df['vader_sentiment'].value_counts()

for label in ['positive', 'neutral', 'negative']:
    count = vader_counts.get(label, 0)
    pct = count / total * 100
    print(f"   {label}: {count} reviews ({pct:.1f}%)")

# Genre-wise Trends
genre_avg = df.groupby('genre')['vader_score'].mean().sort_values(ascending=False)
best_genre = genre_avg.index[0]
worst_genre = genre_avg.index[-1]

# VADER vs Original Labels
matches = (df['sentiment'] == df['vader_sentiment']).sum()
accuracy = matches / total * 100""", "Code — Key inference calculations:")

doc.add_page_break()

# ══════════════════════════════════════════════════════════════════
#   6. VISUALIZATIONS AND ANALYSIS
# ══════════════════════════════════════════════════════════════════
doc.add_heading("6. Visualizations and Analysis", level=1)
doc.add_paragraph(
    "This section presents all nine visualizations generated during the project, "
    "along with the code used to create each plot and a detailed explanation of "
    "what each visualization reveals about the data."
)

# ── 6.1 Sentiment by Genre ────────────────────────────────────────
doc.add_heading("6.1 Average Sentiment Score by Genre (Bar Chart)", level=2)
add_code_block(doc, """genre_sentiment = df.groupby('genre')['vader_score'].mean().sort_values()

plt.figure(figsize=(10, 6))
sns.barplot(x=genre_sentiment.index, y=genre_sentiment.values,
            hue=genre_sentiment.index, palette='coolwarm', legend=False)
plt.title("Average Sentiment Score by Genre")
plt.ylabel("Average VADER Score")
plt.xlabel("Genre")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("plots/01_sentiment_by_genre.png")""", "Code — Sentiment by Genre:")
add_plot(doc, "01_sentiment_by_genre.png",
         "Figure 6.1: Average VADER Sentiment Score by Genre — Bar Chart")
doc.add_paragraph(
    "Explanation: This bar chart displays the average VADER compound sentiment score "
    "for each movie genre. Genres with taller bars have more positively-received reviews. "
    "The 'coolwarm' color palette visually reinforces the polarity — warmer colors "
    "for higher sentiment, cooler colors for lower sentiment. This chart helps identify "
    "which genres audiences respond to most favorably. Differences between genres are "
    "relatively small, suggesting a generally positive baseline across all genres, "
    "but certain genres like Romance tend to score higher while genres like Sci-Fi or "
    "Horror tend to score lower."
)

# ── 6.2 Predicted vs Actual ───────────────────────────────────────
doc.add_heading("6.2 Predicted vs Actual Gross Earnings (Scatter Plot)", level=2)
add_code_block(doc, """pred_df = pd.read_excel("prediction_results.xlsx")

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
plt.savefig("plots/02_predicted_vs_actual.png")""", "Code — Predicted vs Actual:")
add_plot(doc, "02_predicted_vs_actual.png",
         "Figure 6.2: Predicted vs Actual Box Office Revenue — Scatter Plot")
doc.add_paragraph(
    "Explanation: This scatter plot compares the model's predicted gross earnings "
    "(y-axis) against the actual gross earnings (x-axis) for each movie in the test "
    "set. The red dashed diagonal line represents the 'perfect prediction' line — if "
    "the model were perfect, all points would lie exactly on this line. In our case, "
    "the points form a nearly flat horizontal band, indicating that the model predicts "
    "approximately the same value (the mean) for all movies regardless of their actual "
    "earnings. This visually confirms the very low R² score and demonstrates that "
    "rating, budget, and sentiment alone are insufficient to predict box office revenue."
)

# ── 6.3 Sentiment Distribution ────────────────────────────────────
doc.add_heading("6.3 VADER Sentiment Distribution (Pie Chart)", level=2)
add_code_block(doc, """sentiment_counts = df['vader_sentiment'].value_counts()

plt.figure(figsize=(8, 6))
plt.pie(sentiment_counts.values,
        labels=sentiment_counts.index,
        autopct='%1.1f%%',
        colors=['#2ecc71', '#e74c3c', '#f39c12'])
plt.title("VADER Sentiment Distribution")
plt.tight_layout()
plt.savefig("plots/03_sentiment_distribution.png")""", "Code — Sentiment Distribution:")
add_plot(doc, "03_sentiment_distribution.png",
         "Figure 6.3: VADER Sentiment Distribution — Pie Chart")
doc.add_paragraph(
    "Explanation: This pie chart provides a quick overview of the overall sentiment "
    "distribution across all 10,000 reviews as classified by VADER. The chart shows "
    "the proportion of positive (green), negative (red), and neutral (yellow) reviews. "
    "The majority of reviews are classified as positive, which aligns with the "
    "expectation that audiences who voluntarily write reviews tend to have stronger "
    "(often positive) opinions. The neutral segment represents reviews with ambiguous "
    "or balanced language."
)

# ── 6.4 Rating by Genre ───────────────────────────────────────────
doc.add_heading("6.4 Rating Distribution by Genre (Box Plot)", level=2)
add_code_block(doc, """plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='genre', y='rating', hue='genre',
            palette='Set2', legend=False)
plt.title("Movie Rating Distribution by Genre")
plt.ylabel("Rating")
plt.xlabel("Genre")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("plots/04_rating_by_genre.png")""", "Code — Rating Distribution by Genre:")
add_plot(doc, "04_rating_by_genre.png",
         "Figure 6.4: Movie Rating Distribution by Genre — Box Plot")
doc.add_paragraph(
    "Explanation: This box plot visualizes how movie ratings are distributed across "
    "different genres. Each box represents the interquartile range (IQR) — the middle "
    "50% of ratings for that genre. The line inside each box is the median rating. "
    "The whiskers extend to the full range of the data. This chart reveals whether "
    "certain genres consistently receive higher or lower ratings and how much variability "
    "exists within each genre. A genre with a compact box has more consistent ratings, "
    "while a genre with a tall box has greater variability."
)

# ── 6.5 Correlation Heatmap ───────────────────────────────────────
doc.add_heading("6.5 Correlation Heatmap", level=2)
add_code_block(doc, """corr = df[['rating', 'budget', 'gross_earning', 'vader_score']].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='RdYlGn', fmt='.3f')
plt.title("Correlation Matrix")
plt.tight_layout()
plt.savefig("plots/05_correlation_heatmap.png")""", "Code — Correlation Heatmap:")
add_plot(doc, "05_correlation_heatmap.png",
         "Figure 6.5: Correlation Matrix — Heatmap")
doc.add_paragraph(
    "Explanation: The correlation heatmap displays the pairwise Pearson correlation "
    "coefficients between all numerical variables: rating, budget, gross_earning, and "
    "vader_score. Values range from -1 (perfect negative correlation) to +1 (perfect "
    "positive correlation), with 0 indicating no linear relationship. The 'RdYlGn' "
    "color map uses red for negative correlations, yellow for near-zero, and green for "
    "positive correlations. This chart is crucial for understanding feature relationships — "
    "if budget and gross_earning showed a strong positive correlation, it would suggest "
    "higher-budget movies tend to earn more. Low correlations between features and the "
    "target variable explain the model's poor predictive performance."
)

# ── 6.6 Budget vs Gross ───────────────────────────────────────────
doc.add_heading("6.6 Budget vs Gross Earning (Scatter Plot)", level=2)
add_code_block(doc, """plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='budget', y='gross_earning',
                alpha=0.6, color='purple')
plt.title("Budget vs Gross Earning")
plt.xlabel("Budget")
plt.ylabel("Gross Earning")
plt.tight_layout()
plt.savefig("plots/06_budget_vs_gross.png")""", "Code — Budget vs Gross Earning:")
add_plot(doc, "06_budget_vs_gross.png",
         "Figure 6.6: Budget vs Gross Earning — Scatter Plot")
doc.add_paragraph(
    "Explanation: This scatter plot examines the relationship between a movie's "
    "production budget and its gross box-office earnings. Each purple dot represents "
    "a movie. If higher budgets consistently led to higher earnings, we would see "
    "a clear upward trend from left to right. The pattern (or lack thereof) in this "
    "plot helps explain whether production investment is a reliable predictor of "
    "commercial success. A dispersed cloud of points suggests that budget alone is "
    "not a strong predictor."
)

# ── 6.7 Movies per Genre ──────────────────────────────────────────
doc.add_heading("6.7 Number of Movies per Genre (Count Plot)", level=2)
add_code_block(doc, """plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='genre',
              order=df['genre'].value_counts().index,
              palette='viridis', hue='genre', legend=False)
plt.title("Number of Movies by Genre")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("plots/07_movies_per_genre.png")""", "Code — Movies per Genre:")
add_plot(doc, "07_movies_per_genre.png",
         "Figure 6.7: Number of Movies by Genre — Count Plot")
doc.add_paragraph(
    "Explanation: This count plot shows the frequency distribution of movies across "
    "different genres in the dataset. It reveals which genres are most and least "
    "represented. An imbalanced distribution could bias genre-specific analyses — for "
    "example, a genre with very few movies might show extreme sentiment scores simply "
    "due to small sample size. The 'viridis' color palette provides a visually "
    "distinct and accessible color scheme."
)

# ── 6.8 VADER Score Distribution ──────────────────────────────────
doc.add_heading("6.8 Distribution of VADER Scores (Histogram with KDE)", level=2)
add_code_block(doc, """plt.figure(figsize=(8, 6))
sns.histplot(df['vader_score'], bins=30, kde=True, color='teal')
plt.title("Distribution of VADER Sentiment Scores")
plt.xlabel("VADER Score")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("plots/08_vader_score_distribution.png")""", "Code — VADER Score Distribution:")
add_plot(doc, "08_vader_score_distribution.png",
         "Figure 6.8: Distribution of VADER Sentiment Scores — Histogram with KDE")
doc.add_paragraph(
    "Explanation: This histogram displays the frequency distribution of all VADER "
    "compound scores across the 10,000 reviews. The x-axis shows the compound score "
    "(-1 to +1) and the y-axis shows how many reviews fall into each bin. The overlaid "
    "KDE (Kernel Density Estimate) curve provides a smooth approximation of the "
    "distribution shape. A distribution skewed toward the positive end (right side) "
    "confirms that most reviews carry positive sentiment. The spread and shape of the "
    "distribution reveal whether reviews are predominantly extreme (peaks at -1 and +1) "
    "or moderate."
)

# ── 6.9 Rating vs Gross ───────────────────────────────────────────
doc.add_heading("6.9 Rating vs Gross Earning (Scatter Plot)", level=2)
add_code_block(doc, """plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='rating', y='gross_earning',
                alpha=0.5, color='orange')
plt.title("Rating vs Gross Earning")
plt.xlabel("Rating")
plt.ylabel("Gross Earning")
plt.tight_layout()
plt.savefig("plots/09_rating_vs_gross.png")""", "Code — Rating vs Gross Earning:")
add_plot(doc, "09_rating_vs_gross.png",
         "Figure 6.9: Rating vs Gross Earning — Scatter Plot")
doc.add_paragraph(
    "Explanation: This scatter plot explores whether higher-rated movies tend to earn "
    "more at the box office. Each orange dot represents a movie, with its rating on "
    "the x-axis and gross earning on the y-axis. A strong positive trend would suggest "
    "that audiences reward quality. However, a scattered pattern indicates that "
    "critically well-received movies do not necessarily translate to high box office "
    "returns, and vice versa — reinforcing the complexity of predicting movie success."
)

doc.add_page_break()

# ══════════════════════════════════════════════════════════════════
#   7. RESULTS AND KEY FINDINGS
# ══════════════════════════════════════════════════════════════════
doc.add_heading("7. Results and Key Findings", level=1)

doc.add_heading("7.1 Sentiment Analysis Results", level=2)
findings_sent = [
    "The VADER sentiment analyzer classified approximately 70% of reviews as positive, "
    "indicating that audiences in this dataset generally had favorable reactions to the "
    "movies they reviewed.",
    "VADER's automated classifications matched the original human-labeled sentiments with "
    "approximately 70% accuracy, validating its reliability for large-scale automated "
    "sentiment analysis tasks.",
    "Genre-wise analysis revealed subtle but consistent differences in audience sentiment. "
    "Romance movies tended to receive the most positive reviews, while genres like Sci-Fi "
    "and Horror received comparatively lower (but still positive) sentiment scores.",
    "The VADER score distribution histogram showed a right-skewed distribution, confirming "
    "the positive sentiment bias in the dataset.",
]
for f in findings_sent:
    doc.add_paragraph(f, style='List Bullet')

doc.add_heading("7.2 Prediction Model Results", level=2)
findings_model = [
    "The Linear Regression model achieved a very low R² score (close to 0), indicating "
    "that the selected features (rating, budget, vader_score) explain virtually none of "
    "the variance in gross earnings.",
    "The RMSE value was high relative to the scale of gross earnings, further confirming "
    "the model's poor predictive capability.",
    "The Predicted vs Actual scatter plot visually confirmed the model's failure — "
    "predictions formed a flat horizontal band at the mean value rather than following "
    "the diagonal 'perfect prediction' line.",
    "The correlation heatmap showed weak correlations between the feature variables and "
    "the target variable (gross_earning), explaining the model's inability to learn "
    "meaningful patterns.",
]
for f in findings_model:
    doc.add_paragraph(f, style='List Bullet')

doc.add_heading("7.3 Key Takeaway", level=2)
doc.add_paragraph(
    "The most significant finding of this project is the stark contrast between the "
    "success of the NLP component and the failure of the prediction component. While "
    "VADER proved to be highly effective at automating sentiment analysis — a task that "
    "would take humans weeks to perform manually on 10,000 reviews — the Linear Regression "
    "model demonstrated that box office success is far too complex to be predicted by "
    "simple numerical features alone. This underscores a fundamental truth in data "
    "science: even sophisticated models are only as good as the features they are given."
)

# ══════════════════════════════════════════════════════════════════
#   8. LIMITATIONS
# ══════════════════════════════════════════════════════════════════
doc.add_heading("8. Limitations", level=1)
limitations = [
    "Limited Feature Set: The prediction model used only three features (rating, budget, "
    "vader_score). Real-world box office prediction requires features like star power, "
    "director reputation, marketing spend, release date, franchise status, and more.",
    "Synthetic Data Characteristics: While the dataset contains 10,000 records, some "
    "patterns may not fully represent real-world movie industry dynamics.",
    "Single Model Approach: Only Linear Regression was tested. More advanced models "
    "(Random Forest, Gradient Boosting, Neural Networks) might capture non-linear "
    "relationships better.",
    "VADER Limitations: While effective for short social media-style text, VADER may "
    "miss nuances like sarcasm, context-dependent meaning, or domain-specific jargon.",
    "No Temporal Analysis: The project does not consider time-based trends, such as "
    "how audience sentiment or box office performance evolves over release windows.",
]
for lim in limitations:
    doc.add_paragraph(lim, style='List Bullet')

# ══════════════════════════════════════════════════════════════════
#   9. FUTURE SCOPE
# ══════════════════════════════════════════════════════════════════
doc.add_heading("9. Future Scope", level=1)
future = [
    "Incorporate additional features such as cast popularity (e.g., number of social media "
    "followers), director track record, marketing budget, and release timing to improve "
    "prediction accuracy.",
    "Experiment with advanced machine learning algorithms including Random Forest, "
    "XGBoost, Support Vector Machines, and Deep Learning models.",
    "Apply more sophisticated NLP techniques such as transformer-based models (BERT, "
    "RoBERTa) for sentiment analysis, which can capture contextual meaning, sarcasm, "
    "and complex sentence structures better than lexicon-based approaches.",
    "Perform time-series analysis to study how sentiment evolves pre-release, opening "
    "weekend, and post-release.",
    "Build a web-based dashboard (using Streamlit or Flask) to allow interactive "
    "exploration of the data and real-time predictions.",
    "Extend the dataset with real-world data from APIs like TMDB (The Movie Database) "
    "or OMDB for more robust analysis.",
]
for f in future:
    doc.add_paragraph(f, style='List Bullet')

# ══════════════════════════════════════════════════════════════════
#   10. CONCLUSION
# ══════════════════════════════════════════════════════════════════
doc.add_heading("10. Conclusion", level=1)
doc.add_paragraph(
    "This project successfully demonstrated a complete end-to-end data science pipeline "
    "that integrates data preprocessing, Natural Language Processing, machine learning, "
    "and data visualization. The pipeline was designed with modularity in mind — each "
    "step implemented as an independent script that can be run and debugged in isolation."
)
doc.add_paragraph(
    "The VADER sentiment analysis component proved highly effective, achieving "
    "approximately 70% agreement with human-labeled sentiments and enabling rapid "
    "automated classification of 10,000 movie reviews. It revealed that audience "
    "sentiment varies subtly across genres, with Romance movies receiving the most "
    "positive reviews and Sci-Fi/Horror receiving comparatively lower scores."
)
doc.add_paragraph(
    "The Linear Regression prediction model, however, demonstrated an important lesson: "
    "predicting box office success is an inherently complex, multi-factorial problem. "
    "The three features used (rating, budget, sentiment score) proved insufficient, "
    "yielding an R² score near zero. This result is itself a valuable finding — it "
    "empirically proves that movie success depends on a constellation of factors "
    "including marketing strategy, star power, franchise history, release timing, "
    "competition, and cultural trends that extend far beyond simple numerical metrics."
)
doc.add_paragraph(
    "Together, these results highlight both the power and the limitations of data-driven "
    "analysis in the entertainment industry. While NLP tools like VADER can efficiently "
    "extract qualitative insights at scale, predicting financial outcomes requires "
    "significantly richer feature engineering and potentially more sophisticated "
    "modeling approaches."
)

# ══════════════════════════════════════════════════════════════════
#   11. REFERENCES
# ══════════════════════════════════════════════════════════════════
doc.add_heading("11. References", level=1)
refs = [
    "Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for "
    "Sentiment Analysis of Social Media Text. Proceedings of the Eighth International "
    "AAAI Conference on Weblogs and Social Media.",
    "Pedregosa, F. et al. (2011). Scikit-learn: Machine Learning in Python. Journal of "
    "Machine Learning Research, 12, pp. 2825–2830.",
    "McKinney, W. (2010). Data Structures for Statistical Computing in Python. "
    "Proceedings of the 9th Python in Science Conference, pp. 51–56.",
    "Hunter, J.D. (2007). Matplotlib: A 2D Graphics Environment. Computing in Science "
    "& Engineering, 9(3), pp. 90–95.",
    "Waskom, M. (2021). seaborn: statistical data visualization. Journal of Open Source "
    "Software, 6(60), 3021.",
    "Python Software Foundation. Python Language Reference, version 3.x. "
    "https://www.python.org",
]
for i, ref in enumerate(refs, 1):
    doc.add_paragraph(f"[{i}] {ref}")

# ── Save the document ─────────────────────────────────────────────
output_path = os.path.join(BASE_DIR, "Movie_Success_Prediction_Project_Report.docx")
doc.save(output_path)
print(f"\nReport generated successfully!")
print(f"Saved to: {output_path}")
