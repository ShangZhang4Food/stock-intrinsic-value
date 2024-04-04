# Intrinsic stock value estimator

Intrinsic value is a crucial concept in investing. It represents the fundamental, objective value of a stock, independent of market fluctuations. This repository is to automatically download historical financial information of a chosen stock, estimate the intrinsic value with well known methodologies, and showcase the gap between current stock price and the intrinsic value of this stock. 

The following are methods that this streamlit app is capable of . 

1. **Price-to-Earnings (P/E) Ratio**:
    - The P/E ratio compares a company’s stock price to its earnings per share (EPS) over the past 12 months.
    - A low P/E ratio suggests better value, while a high P/E ratio may indicate overvaluation.

2. **Discounted Cash Flow (DCF) Model**:
    - Estimate a company’s future cash flow (usually for the next 10 years).
    - Discount these cash flows to present value using a discount rate (considering inflation).

3. **Price-Earnings Relative (P/E Relative)**:
    - Divide a company’s P/E ratio by the market’s P/E ratio or its industry’s average P/E ratio.
    - A value above 1.0 indicates the company’s P/E ratio is typically higher than the market’s, and vice versa.

3. **Ben Graham’s Formula**:
    - Determine the trailing 12-month EPS of the company.
    - Multiply the company’s long-term growth rate by 2 and add 8.5 to it.
    - Find the product of the value obtained in step 2 with the EPS of the company and a factor of 4.4.

To run the streamlit app: 
