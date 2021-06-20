-- 4.1) trigger for deleting from cart_product
CREATE OR REPLACE FUNCTION delete_cart_product()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
	DELETE FROM cart_product WHERE cart_product.cart_id = OLD.cart_id;
	DELETE FROM orders WHERE cart_id = OLD.cart_id;
	RETURN OLD;
END;
$$;

CREATE TRIGGER delete_cart
	BEFORE DELETE ON carts
	FOR EACH ROW
	EXECUTE PROCEDURE delete_cart_product();

-- checking for working
BEGIN;

SELECT * FROM orders WHERE order_id = 22;

SELECT * FROM orders o
JOIN carts c USING (cart_id)
JOIN cart_product cp USING (cart_id)
JOIN products p USING (product_id)
WHERE cp.cart_id = 22;

DELETE FROM carts WHERE cart_id = 22;
ROLLBACK;


-- 4.2) trigger for updating order
CREATE OR REPLACE FUNCTION order_updating()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
     UPDATE orders SET updated_at = now() 
	 WHERE order_id = NEW.order_id;
     RETURN NEW;
END;
$$;

CREATE TRIGGER order_update
     AFTER UPDATE OF order_id, cart_id, order_status_id, shipping_total, total, created_at
     ON orders
     FOR EACH ROW
     EXECUTE PROCEDURE order_updating();
	 
-- checking for working
BEGIN;
SELECT * FROM orders WHERE order_id = 40;
update orders set shipping_total = 700 WHERE order_id = 40;
ROLLBACK;