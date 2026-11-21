SELECT
    CAST(order_timestamp AS DATE) AS order_date,
    COUNT(DISTINCT order_id) AS order_count,
    SUM(order_amount) AS gross_revenue
FROM analytics.orders
WHERE order_timestamp >= CURRENT_DATE - INTERVAL '7' DAY
GROUP BY CAST(order_timestamp AS DATE)
ORDER BY order_date;
