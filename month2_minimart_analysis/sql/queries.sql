-- SQL queries for retrieving insights
SELECT *
FROM customers;


SELECT * 
FROM products
WHERE category = "Drinks";

SELECT * 
FROM orders
ORDER BY order_date DESC;

-- AGGREGATION
SELECT COUNT(*) AS total_orders
FROM orders;

SELECT (SUM(price * quantity)) AS total_revenue
FROM orders;

SELECT AVG(price) AS avg_product_price
FROM products;

-- JOINS
SELECT c.name as customer_name, p.product_name as product_name, o.quantity as quantity, o.order_date as order_date
FROM customers as c
INNER JOIN orders as o ON c.customer_id = o.customer_id
INNER JOIN products as p ON o.product_id = p.product_id;

SELECT c.customers, COUNT(o.order_id) AS total_orders
FROM customers as c 
LEFT JOIN orders as o ON c.customer_id = o.customer_id
GROUP BY c.customer_id;

SELECT p.product_name, p.price, o.quantity, o.order_date
FROM products as p
LEFT JOIN orders as o ON p.product_id = o.product_id;