# Model Evaluation and Confidence Summary

The forecasting model developed for LASA Financial Services leverages **Facebook Prophet**, a probabilistic time-series model capable of capturing both trend and seasonality in financial data. The model was trained on 5 years of daily price data for the NIFTY 50 and NIFTY BANK indices fetched from Yahoo Finance.

**Confidence and Performance:**  
Prophet demonstrated strong performance for short-term forecasts (1–3 months), successfully identifying recent market momentum and cyclic behavior. The model’s built-in confidence intervals (95% CI) provide a realistic range of potential future values, indicating moderate confidence in short-term projections. For long-term forecasts (1–3 years), confidence naturally decreases as uncertainty compounds over time, which is reflected in the widening prediction intervals.

**Key Assumptions:**  
- Market trends and seasonality patterns observed in the past continue into the future.  
- No major structural or policy shocks alter the underlying economic drivers.  
- Data retrieved from Yahoo Finance is accurate and complete.  

**Risks and Limitations:**  
- Financial markets are influenced by unforeseen macroeconomic, political, or global events that Prophet cannot anticipate.  
- The model does not incorporate exogenous variables (e.g., interest rates, inflation) that may impact price movements.  
- Overfitting or underfitting may occur during volatile market periods.  

**Conclusion:**  
Despite these limitations, Prophet provides interpretable and probabilistic insights into market direction. Its forecasts are valuable for trend analysis and scenario planning but should be complemented with expert judgment, external data, and real-time market intelligence before making investment decisions.
