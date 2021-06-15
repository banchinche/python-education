-- first
-- show name and email potential and existing customers
SELECT name, email
FROM potential_customers
WHERE city = 'city 17'
UNION
SELECT first_name, email
FROM users
WHERE city = 'city 17';

-- second
-- show sorted first_name and email from all users
SELECT first_name, email
FROM users
ORDER BY first_name, email;


-- third
-- show count of each category product sorted in descent order
SELECT category_title, COUNT(*) AS category_counts
FROM categories c
INNER JOIN products p
	ON p.category_id = c.category_id
GROUP BY category_title
ORDER BY category_counts DESC;


-- fourth
-- 1) show all product not in cart
SELECT product_title
FROM products EXCEPT(
	SELECT product_title
 	FROM products p INNER JOIN cart_product c
 		ON p.product_id = c.product_id
);
-- 2) show all products weren't in orders (probably in carts)
SELECT product_title
FROM products p1 EXCEPT(
	SELECT p2.product_title
 	FROM products p2
 		INNER JOIN cart_product cp ON p2.product_id = cp.product_id
 		INNER JOIN carts c ON c.cart_id = cp.cart_id
 		INNER JOIN orders o ON o.cart_id = c.cart_id
);
-- 3) show top 10 added products (in cart)
SELECT product_title, COUNT(*)
FROM products p
INNER JOIN cart_product cp
	ON p.product_id = cp.product_id
GROUP BY p.product_title
ORDER BY COUNT(*) DESC
LIMIT 10;
-- 4) show top 10 added products (in orders)
SELECT p.product_title, COUNT(o.order_id) AS order_counts
FROM products p
 	INNER JOIN cart_product cp  ON p.product_id = cp.product_id
 	INNER JOIN carts c ON c.cart_id = cp.cart_id
 	INNER JOIN orders o ON o.cart_id = c.cart_id
GROUP BY p.product_title
ORDER BY order_counts DESC
LIMIT 10;
-- 5) show top 5 total spent in order
SELECT u.user_id, u.first_name, SUM(o.total) FROM users u
	INNER JOIN carts c ON u.user_id = c.cart_id
 	INNER JOIN orders o ON o.cart_id = c.cart_id
	INNER JOIN order_status os ON os.order_status_id = o.order_status_id
WHERE os.order_status_id = 4
GROUP BY u.user_id
ORDER BY SUM(o.total) DESC
LIMIT 5;
-- 6) show top 5 active users (most count of orders)
SELECT u.user_id, u.first_name, COUNT(o.order_id) FROM users u
	INNER JOIN carts c ON u.user_id = c.cart_id
	INNER JOIN orders o ON o.cart_id = c.cart_id
GROUP BY u.user_id
ORDER BY COUNT(o.order_id) DESC
LIMIT 5;
-- 7) show top 5 users with carts but no order (highest total)
SELECT u.user_id, u.first_name, o.order_id, SUM(o.total) FROM users u
INNER JOIN carts c ON u.user_id = c.cart_id
INNER JOIN orders o ON o.cart_id = c.cart_id
WHERE o.order_status_id IS null OR o.order_status_id NOT IN (1, 2, 3, 4, 5)
GROUP BY u.user_id, o.order_id
ORDER BY SUM(o.total) DESC
LIMIT 5;
