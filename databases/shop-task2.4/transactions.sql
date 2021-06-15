-- INSERTS
-- 1) with commit
BEGIN;
INSERT INTO cart_product VALUES(2, 900);
COMMIT;
-- 2) with rollback
BEGIN;
INSERT INTO carts VALUES (2001, 5, 1023.23, 1023.23, '2021-03-13 07:53:43');
ROLLBACK;
-- 3) with rollback to savepoint
BEGIN;
SAVEPOINT save_point1;
INSERT INTO categories(category_id, category_title, category_description) 
VALUES (21, 'category 21', 'catergory 21 desc');
ROLLBACK TO SAVEPOINT save_point1;

-- UPDATES
-- 1) with commit
BEGIN;
UPDATE potential_customers
SET name = 'third-first-name'
WHERE name = 'example-name3';
COMMIT;
-- 2) with rollback
BEGIN;
UPDATE categories
SET category_title = 'New-category'
WHERE category_title = 'Category 20';
ROLLBACK;
-- 3) with rollback to savepoint
BEGIN;
SAVEPOINT save_point3;
UPDATE orders
SET total = 50
WHERE total < 50;
ROLLBACK TO SAVEPOINT save_point3;

-- DELETES
-- 1) with commit
BEGIN;
DELETE FROM cart_product WHERE cart_id = 20;
COMMIT;
-- 2) with rollback
BEGIN;
DELETE FROM potential_customers WHERE pot_customer_id BETWEEN 30 AND 41;
ROLLBACK;
-- 3) with rollback to savepoint
BEGIN;
SAVEPOINT save_point2;
DELETE FROM orders WHERE cart_id = 4;
ROLLBACK TO SAVEPOINT save_point2;