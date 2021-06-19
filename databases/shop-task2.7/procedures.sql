-- 2.1) inserts category
CREATE OR REPLACE PROCEDURE insert_category(cat_id INT, cat_title VARCHAR, cat_desc TEXT)
LANGUAGE plpgsql
AS $$
DECLARE
	categories_count INT;
BEGIN
	SELECT COUNT(*)
	INTO categories_count
	FROM categories;
	IF cat_id <= categories_count THEN
		RAISE EXCEPTION 'Duplicate key value %', cat_id;
		ROLLBACK;
	ELSE
		INSERT INTO categories VALUES (cat_id, cat_title, cat_desc);
		COMMIT;
	END IF;
END;
$$;

-- checking queries
SELECT * FROM categories;

CALL insert_category(21, 'Category 21', 'Category 21 desc.');
DROP PROCEDURE insert_category;

BEGIN;
DELETE FROM categories WHERE category_id = 21;
ROLLBACK;
COMMIT;


-- 2.2) loop usage in procedure (inserts product id's to certain cart)
CREATE OR REPLACE PROCEDURE insert_products_to_cart(cart_num INT, prod_low INT, prod_high INT)
LANGUAGE plpgsql
AS $$
BEGIN
    -- doesn't work !!!
 	SELECT cart_num, generate_series(prod_low, prod_high) AS product_id
 	FROM generate_series(1, prod_high - prod_low) AS ser_prods;
	INSERT INTO cart_product (cart_id, product_id)
	SELECT cart_num, product_id FROM ser_prods;
	COMMIT;
END;
$$;

-- checking queries
BEGIN;
CALL insert_products_to_cart(40, 20, 25);
DROP PROCEDURE insert_products_to_cart;

SELECT * FROM cart_product
WHERE cart_id = 40
ORDER BY product_id ASC;
ROLLBACK;
