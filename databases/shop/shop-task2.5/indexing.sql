SELECT
    tablename,
    indexname,
    indexdef
FROM
    pg_indexes
WHERE
    schemaname = 'public'
ORDER BY
    tablename,
    indexname;

-- 1)
-- worse...
CREATE INDEX idx_order_status_hash ON orders USING hash(order_status_id);
-- little bit better than sequence scan
CREATE INDEX idx_order_status_tree ON orders USING btree(order_status_id);
-- best of these three
CREATE INDEX idx_order_status_id ON orders(order_status_id);

SET enable_seqscan = OFF;
SET enable_seqscan = ON;

EXPLAIN(ANALYSE) SELECT * FROM orders WHERE order_status_id = 4;

DROP INDEX idx_order_status_id;
DROP INDEX idx_order_status_hash;
DROP INDEX idx_order_status_tree;


-- 2)
-- btree is fine with text patterns
-- this better than seqscan
CREATE UNIQUE INDEX idx_product_title ON products USING btree(product_title);

EXPLAIN(ANALYSE) SELECT * FROM products
WHERE product_title = '%title';

DROP INDEX idx_product_title;


-- 3)
-- averages better than seqscan (0.28-338.68) (sort 263.26-270.76 + seqscan 0-90)
-- but optimizer selects seqscan anyway
CREATE INDEX idx_user_fname ON users USING hash(first_name);
CREATE INDEX idx_user_fname ON users(first_name ASC NULLS LAST);
CREATE INDEX idx_user_fname ON users(first_name DESC NULLS FIRST);

SET enable_seqscan = OFF;
SET enable_seqscan = ON;

EXPLAIN SELECT * FROM users ORDER BY first_name ASC;
EXPLAIN SELECT * FROM users ORDER BY first_name DESC;

DROP INDEX idx_user_fname;