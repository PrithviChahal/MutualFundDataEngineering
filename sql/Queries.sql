Select
    scheme_name,
    aum_crore
From fact_performance
Order By aum_crore Desc
Limit 5;



Select
    strftime('%Y-%m', date) As month,
    AVG(nav) As avg_nav
From fact_nav
Group By month
Order By month;



Select
    state,
    COUNT(*) As total_transactions
From fact_transactions
Group By state
Order By total_transactions Desc;



Select
    scheme_name,
    expense_ratio_pct
From fact_performance
Where expense_ratio_pct < 1;



Select
    SUM(amount_inr)
From fact_transactions
Where transaction_type='SIP';



Select
    transaction_type,
    COUNT(*)
From fact_transactions
Group By transaction_type;



Select
    AVG(return_1yr_pct)
From fact_performance;



Select
    fund_house,
    COUNT(*)
From dim_fund
Group By fund_house
Order BY COUNT(*) Desc
Limit 5;



Select
    payment_mode,
    AVG(amount_inr)
From fact_transactions
Group By payment_mode;



Select
    gender,
    COUNT(Distinct investor_id)
From fact_transactions
Group By gender;