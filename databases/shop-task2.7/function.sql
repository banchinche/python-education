-- 1.1) sets shipping total if user's city is x_city
CREATE OR REPLACE FUNCTION user_xcity_zero_shipping (x_city VARCHAR)
RETURNS void
LANGUAGE plpgsql
AS $$
BEGIN
	IF EXISTS(
		SELECT 1 FROM users
     	WHERE city = x_city
	) THEN
		UPDATE orders SET shipping_total = 0
		WHERE cart_id IN (SELECT o.cart_id
		FROM users u
		JOIN carts c USING (user_id)
		JOIN orders o USING (cart_id) WHERE u.city = x_city);
     ELSE
         RAISE EXCEPTION 'There is no such % city.', x_city;
     END IF;
END;
$$;
DROP FUNCTION user_xcity_zero_shipping;


-- checking update and exception handling
BEGIN;

SELECT user_xcity_zero_shipping('city 2');
SELECT user_xcity_zero_shipping('city 3500');

SELECT u.city, o.shipping_total
FROM users u
JOIN carts c USING (user_id)
JOIN orders o USING (cart_id) WHERE u.city = 'city 2';

ROLLBACK; 

