# Data Dictionary

This document describes all datasets, columns, data types, and business definitions used in the Mutual Fund Data Engineering project.


## fund_master.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | INTEGER | Unique mutual fund identifier issued by AMFI |
| fund_house | TEXT | Name of the Asset Management Company |
| scheme_name | TEXT | Name of the mutual fund scheme |
| category | TEXT | Mutual fund category |
| sub_category | TEXT | Sub-category of the scheme |
| plan | TEXT | Direct or Regular plan |
| launch_date | DATE | Scheme launch date |
| benchmark | TEXT | Benchmark index of the scheme |
| expense_ratio_pct | REAL | Expense ratio percentage |
| exit_load_pct | REAL | Exit load percentage |
| min_sip_amount | INTEGER | Minimum SIP amount |
| min_lumpsum_amount | INTEGER | Minimum lumpsum investment |
| fund_manager | TEXT | Name of the fund manager |
| risk_category | TEXT | Risk level of the scheme |
| sebi_category_code | TEXT | SEBI category code |



## nav_history.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | INTEGER | Mutual fund AMFI code |
| date | DATE | NAV date |
| nav | REAL | Net Asset Value of the scheme |



## investor_transactions.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| investor_id | TEXT | Unique investor identifier |
| transaction_date | DATE | Date of transaction |
| amfi_code | INTEGER | Mutual fund AMFI code |
| transaction_type | TEXT | SIP, Lumpsum, or Redemption |
| amount_inr | REAL | Transaction amount in INR |
| state | TEXT | Investor state |
| city | TEXT | Investor city |
| city_tier | TEXT | Tier of the city |
| age_group | TEXT | Investor age category |
| gender | TEXT | Investor gender |
| annual_income_lakh | REAL | Annual income in lakhs |
| payment_mode | TEXT | UPI, Cheque, Net Banking, etc. |
| kyc_status | TEXT | KYC verification status |



## scheme_performance.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | INTEGER | Mutual fund AMFI code |
| scheme_name | TEXT | Scheme name |
| fund_house | TEXT | Asset Management Company |
| category | TEXT | Fund category |
| plan | TEXT | Scheme plan |
| return_1yr_pct | REAL | 1-year return percentage |
| return_3yr_pct | REAL | 3-year return percentage |
| return_5yr_pct | REAL | 5-year return percentage |
| benchmark_3yr_pct | REAL | Benchmark 3-year return |
| alpha | REAL | Alpha of the fund |
| beta | REAL | Beta of the fund |
| sharpe_ratio | REAL | Sharpe ratio |
| sortino_ratio | REAL | Sortino ratio |
| std_dev_ann_pct | REAL | Annualized standard deviation |
| max_drawdown_pct | REAL | Maximum drawdown percentage |
| aum_crore | REAL | Assets Under Management in crores |
| expense_ratio_pct | REAL | Expense ratio percentage |
| morningstar_rating | INTEGER | Morningstar rating |
| risk_grade | TEXT | Risk grade of the fund |