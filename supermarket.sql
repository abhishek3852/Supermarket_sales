--ANS ! Sales PRofit and insight
SELECT 
category,
COUNT(*) AS Number_of_rows,
AVG(sales) AS average_sales,
MAX(sales) As max_sales,
MIN(sales) AS min_sales,
SUM(sales) AS total_sales,
FROM practise.supermarket_sales
GROUP BY category

--ANS 2 cusomter insight
SELECT 
customer_name,
COUNT(order_id) AS no_of_orders
From practise.supermarket_sales
GROUP BY customer_name
ORDER BY no_of_orders DESC LIMIT 1;

SELECT 
  COUNT(order_id) * 1.0 / COUNT(DISTINCT customer_name) AS avg_order_frequency
FROM practise.supermarket_sales;

SELECT customer_name, COUNT(*)
FROM practise.supermarket_sales
GROUP BY customer_name;

SELECT 
SUM (sales)/ Count(order_id)
FROM practise.supermarket_sales

-- ANS 3 : - ORDER TREND

SELECT 
region,
city,
Count(order_id)
FROM practise.supermarket_sales
GROUP BY region,city
ORDER BY region,city

--ANS 4 PERFORMANCE METRICS
SELECT 
(SUM (profit)/ SUM (sales))*100 AS profit_margin_percentage
FROM practise.supermarket_sales

--ANS 5 PRODUCT TRENDS
SELECT 
category,
MAX(sales) AS max_sales
FROM practise.supermarket_sales
GROUP BY category
ORDER BY max_sales

SELECT 
    category,
    SUM(sales) AS total_sales,
    (SUM(sales) / (SELECT SUM(sales) FROM practise.supermarket_sales)) * 100 AS category_contribution_percentage
FROM practise.supermarket_sales
GROUP BY category;

SELECT 
  category, 
  sub_category, 
  discount, 
  profit
FROM practise.supermarket_sales
WHERE discount >= 0.35
ORDER BY profit ASC;

