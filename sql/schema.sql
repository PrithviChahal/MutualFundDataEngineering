create table dim_fund(
    amfi_code integer primary key,
    scheme_name text,
    fund_house text,
    category text,
    sub_category text,
    plan text,
    risk_category text,
);


create table dim_date(
    date_key integer primary key,
    full_date date,
    day integer,
    month integer,
    year integer,
    quarter integer
);


create table fact_nav (
    nav_id integer primary key autoincrement,
    amfi_code integer,
    date_key integer,
    nav real,
    foreign key (amfi_code)
        references dim_fund(amfi_code),
    foreign key (date_key)
        references dim_date(date_key)
);


create table fact_transactions (
    transaction_id integer primary key autoincrement,
    investor_id text,
    amfi_code integer,
    date_key integer,
    transaction_type text,
    amount_inr real,
    foreign key (amfi_code)
        references dim_fund(amfi_code),
    foreign key (date_key)
        references dim_date(date_key)
);


create table fact_performance (
    performance_id integer primary key autoincrement,
    amfi_code integer,
    return_1yr_pct real,
    return_3yr_pct real,
    return_5yr_pct real,
    alpha real,
    beta real,
    sharpe_ratio real,
    expense_ratio_pct real,
    foreign key (amfi_code)
        references dim_fund(amfi_code)
);


create table fact_aum (
    aum_id integer primary key autoincrement,
    amfi_code integer,
    aum_crore real,
    foreign key (amfi_code)
        references dim_fund(amfi_code)
);