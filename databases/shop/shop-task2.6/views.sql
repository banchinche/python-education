-- 1) create products view
CREATE OR REPLACE VIEW products_view AS (
    SELECT product_id, product_title, in_stock, price
	FROM products
);
SELECT * FROM products_view;


-- 2) create order_status + order view
CREATE OR REPLACE VIEW order_status_order_view AS (
	SELECT o.order_id, o.order_status_id, os.status_name, o.total
	FROM orders o
	INNER JOIN order_status os USING (order_status_id)
);
SELECT * FROM order_status_order_view;
DROP VIEW order_status_order_view;


-- 3) create products + category view
CREATE OR REPLACE VIEW products_category_view AS (
	SELECT p.product_id, p.product_title, p.product_description,
			c.category_id, c.category_title, c.category_description
	FROM products p
	INNER JOIN categories c USING (category_id)
);
SELECT * FROM products_category_view;
DROP VIEW products_category_view;


-- 4) create materialized view for 'heavy' query
CREATE MATERIALIZED VIEW IF NOT EXISTS categories_count AS (
	SELECT category_title, COUNT(*) AS category_counts
	FROM categories c
	INNER JOIN products p
		ON p.category_id = c.category_id
	GROUP BY category_title
	ORDER BY category_counts DESC
);
SELECT * FROM categories_count;
DROP MATERIALIZED VIEW categories_count;
