-- 1. Top 5 funds by AUM
SELECT fund_house, aum_crore
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV per fund
SELECT amfi_code, AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY amfi_code;

-- 3. Monthly average NAV
SELECT substr(date,1,7) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month;

-- 4. Transactions by state
SELECT state, COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 5. Funds with expense ratio < 1%
SELECT amfi_code, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 6. Top 10 schemes by 5-year return
SELECT amfi_code, return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

-- 7. Average transaction amount
SELECT AVG(amount_inr)
FROM fact_transactions;

-- 8. Transaction count by type
SELECT transaction_type, COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

-- 9. Fund count by category
SELECT category, COUNT(*)
FROM dim_fund
GROUP BY category;

-- 10. Average AUM by fund house
SELECT fund_house,
AVG(aum_crore)
FROM fact_aum
GROUP BY fund_house;