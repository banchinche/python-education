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