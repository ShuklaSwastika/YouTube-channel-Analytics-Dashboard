# 📊 YouTube Channel Analytics Dashboard

This project analyzes and visualizes key performance metrics of a YouTube channel using a synthetic dataset of 1200+ Indian videos. Built using Python, Matplotlib, Pandas, and Streamlit.

## 🔍 Project Overview

**Objective:**  
To explore trends and insights across views, likes, dislikes, and comments by visualizing them in charts and summary tables.

**Tools & Tech Stack:**
- Python (Pandas, Matplotlib)
- Google Colab (for analysis)
- Streamlit (for web app dashboard)
- GitHub (for version control & documentation)

## 🧾 Dataset

- 1200+ rows
- Columns: `VideoID`, `Title`, `UploadDate`, `Views`, `Likes`, `Dislikes`, `Comments`
- Simulated Indian YouTube content data  
- Format: CSV


## Project Structure
📦 YouTube-Analytics-Dashboard
├── app.py                 # Streamlit app
├── youtube_data.csv       # Sample dataset (not uploaded here)
├── README.md              # Project documentation
└── colab_notebook.ipynb   # EDA and charts in Colab

## 📈 Key Features

### 📅 1. Views Over Time (Half-Yearly Trend)
- Clean line chart with labels like `Jan–Jun 2020`, `Jul–Dec 2020`, etc.
- Shows clear growth and decline pattern
- Summary table alongside the chart

### 🏆 2. Top 10 Videos by Views
- Displays highest-performing videos with views and upload dates
- Shown in both bar chart and table format

### 🥧 3. Engagement Distribution
- Pie chart showing Likes vs Dislikes vs Comments
- Also available as a year-wise engagement table

### 📋 4. Summary & Metrics
- Total views, likes, dislikes, and comments calculated
- Highlights key engagement trends

## 🌐 Streamlit App

You can run the interactive dashboard locally:

```bash
streamlit run app.py
```

- It includes:
    - File uploader for CSV
    - All visualizations as charts
    - Summary insights with metrics

## 📌 How to Use
- Clone the repository
- Open Colab notebook for analysis
- Or run app.py with Streamlit for dashboard
- Upload your dataset (CSV) or use the provided one. 

## Acknowledgements
Project by Swastika Shukla
Built using tools like Colab, Streamlit, and Matplotlib