-- function with cursor and loop
CREATE OR REPLACE FUNCTION customer_six_house(customer_name VARCHAR)
RETURNS TEXT
LANGUAGE plpgsql
AS $$
DECLARE
results TEXT DEFAULT '';
rec_customer RECORD;
customer_info CURSOR(customer_name VARCHAR)
	FOR SELECT c.first_name, c.last_name, a.city, a.street, a.house
 	FROM customer c
	JOIN address_telephone a ON c.info_id = a.at_id
 	WHERE first_name = customer_name;
BEGIN

OPEN customer_info(customer_name);
LOOP
	FETCH customer_info INTO rec_customer;
	EXIT WHEN NOT FOUND;
	IF rec_customer.house = 6 THEN
		results := 'Name: ' || rec_customer.first_name || ' ' || 
					rec_customer.last_name || ', Location: ' || 
					rec_customer.city || ', ' || rec_customer.street || ', ' || 
					rec_customer.house;
	END IF;
END LOOP;
CLOSE customer_info;
RETURN results;
END; 
$$;

DROP FUNCTION customer_six_house;
SELECT customer_six_house('first-name6');


-- function that returns table containing order details (price, days, total sum and date of order)
CREATE OR REPLACE FUNCTION order_details (ord_id INT)
RETURNS TABLE (
	o_id INT,
	o_days INT,
	o_price MONEY,
	o_sum MONEY,
	o_date TIMESTAMP
)
LANGUAGE PLPGSQL
AS $$
DECLARE
	temp_rec RECORD;
BEGIN
	FOR temp_rec IN (
		SELECT o.order_id, o.renting_days, c.price, o.renting_days*c.price total, o.renting_date
		FROM orders o
		JOIN car c USING (car_id)
		WHERE o.order_id = ord_id
	) LOOP
		o_id := temp_rec.order_id;
		o_days := temp_rec.renting_days;
		o_price := temp_rec.price;
		o_sum := temp_rec.total;
		o_date := temp_rec.renting_date;
		RETURN NEXT;
	END LOOP;
END;
$$;

DROP FUNCTION order_details(integer);
SELECT * FROM order_details(6);
