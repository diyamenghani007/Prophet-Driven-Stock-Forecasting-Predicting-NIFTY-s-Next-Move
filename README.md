# Prophet-Driven Stock Forecasting: Predicting NIFTY’s Next Move

## Overview
This project forecasts short-term (3 months) and long-term (3 years) price trends for **NIFTY 50** and **NIFTY BANK** indices using **Yahoo Finance** data and **Facebook Prophet** for time-series modeling.  
It automatically fetches data, preprocesses it, generates forecasts, and produces visualizations with confidence intervals.

---

## Features
- Fetches 5 years of daily price data for NIFTY 50 (`^NSEI`) and NIFTY BANK (`^NSEBANK`)
- Cleans and preprocesses the dataset (handles missing or invalid values)
- Generates:
  - **Short-term forecasts (3 months)** — Daily granularity
  - **Long-term forecasts (3 years)** — Weekly granularity
- Exports plots (`.png`) and summary report (`.md`)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/lasa_financial_project.git
   cd lasa_financial_project
2. Run the Script:
   python main.py

Check the Results
You’ll find:
-Forecast plots (.png)
-Text reports (report.txt, summary.txt)
-Optionally: CSV files for raw + processed data

---

## Project Structure
LASA_FINANCIAL_PROJECT/
│
├── data/
│   ├── NIFTY_50_data.csv
│   └── NIFTY_BANK_data.csv
│
├── outputs/
│   ├── NIFTY_50_ShortTerm_forecast.png
│   ├── NIFTY_50_LongTerm_forecast.png
│   ├── NIFTY_BANK_ShortTerm_forecast.png
│   ├── NIFTY_BANK_LongTerm_forecast.png
│   ├── report.txt
│   └── summary.txt
│
├── main.py
├── requirements.txt
└── README.md

---

## Libraries Used

yfinance  	- Fetches historical stock data   	-> Easy to use, reliable, but can have missing days
prophet     - Trend + seasonality forecasting  	-> Handles non-linear growth, uncertainty bands
pandas      - Data handling	                    -> Used for cleaning, merging, and transformations
matplotlib	- Visualization                    	-> For line plots and forecast visualization
numpy       -	Numerical computation            	-> Supports Prophet and data processing

---

### Connect
Feel free to explore the repo and connect with me on [LinkedIn](https://www.linkedin.com/in/diya-menghani/) if you have any feedback, suggestions, or would like to collaborate!
If you have any feedback, ideas, or would like to collaborate!

#### Tags
#Finance #TimeSeries #Prophet #DataAnalysis #MachineLearning #Forecasting #PythonProject #NIFTY50 #NIFTYBANK
