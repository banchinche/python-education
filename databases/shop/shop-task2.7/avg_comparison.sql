CREATE TABLE compare_with_avg AS (
	SELECT c.category_title, p.product_title, p.price, AVG(p.price) OVER (PARTITION BY c.category_title)
	FROM products p
	JOIN categories c USING (category_id)
)
SELECT * FROM compare_with_avg;
