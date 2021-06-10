-- Task 2.1
-- 1) select all users
SELECT * FROM users;
-- 2) select all products
SELECT * FROM products;
-- 3) show all order statuses
SELECT * FROM order_status;

-- Task 2.2
-- 1) select all finished orders
SELECT * FROM orders WHERE order_status_id = 4;

-- Task 2.3
-- 1) select all products with price in range 80 < price <= 150
SELECT * FROM products WHERE price > 80 AND price <= 150;
SELECT * FROM products WHERE price BETWEEN 80 AND 150;
-- 2) select all orders that created after 01.10.2020
SELECT * FROM orders WHERE created_at > '10/01/2020';
-- 3) select all orders from first half of the 2020 year
SELECT * FROM orders WHERE created_at > '01/01/2020' AND created_at <= '06/30/2020';
SELECT * FROM orders WHERE created_at BETWEEN '01/01/2020' AND '06/30/2020';
-- 4) select all products from categories (Category 7, Category 11, Category 18)
SELECT * FROM products WHERE category_id IN (7, 11, 18);
SELECT * FROM products WHERE category_id = 7 OR category_id = 11 OR category_id = 18;
-- 5) select all unfinished orders by 31.12.2020
SELECT * FROM orders WHERE order_status_id IN (1, 2, 3) AND updated_at < '01/01/2021';
-- 6) select all created carts without order (cancelled)
SELECT * FROM carts WHERE cart_id IN
   (SELECT cart_id FROM carts EXCEPT SELECT ord.cart_id  FROM orders ord);
