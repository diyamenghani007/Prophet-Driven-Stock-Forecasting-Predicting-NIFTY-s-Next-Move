# LASA Financial Forecasting Project

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
