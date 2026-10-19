-- Churn rate by contract type
SELECT ContractType,
  100.0*SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)/COUNT(*) AS churn_rate_pct
FROM telecom_customers GROUP BY ContractType ORDER BY churn_rate_pct DESC;
