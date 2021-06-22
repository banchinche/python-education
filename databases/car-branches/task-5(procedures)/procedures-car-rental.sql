-- procedure with inserting or updating transaction
CREATE OR REPLACE PROCEDURE insert_or_update_info(in_id INT)
LANGUAGE PLPGSQL
AS $$
DECLARE
	info_counts INT;
	temp_city VARCHAR := '';
	temp_street VARCHAR := '';
	temp_phone VARCHAR := '';
BEGIN
	SELECT COUNT(*) INTO info_counts FROM address_telephone;
	temp_city := 'City' || CAST(in_id AS VARCHAR);
	temp_street := 'Street' || CAST(in_id AS VARCHAR);
	temp_phone := 'Phone' || CAST(in_id AS VARCHAR);
	IF in_id > info_counts THEN
		INSERT INTO address_telephone VALUES(temp_city, temp_street, in_id, temp_phone);
	ELSE
		UPDATE address_telephone
		SET city = temp_city, street = temp_street, house = in_id, telephone = temp_phone
		WHERE at_id = in_id;
	END IF;
	COMMIT;
END;
$$;

SELECT * FROM address_telephone LIMIT 67;
CALL insert_or_update_info(66);
DROP PROCEDURE insert_or_update_info();


-- procedure with deleting transaction
CREATE OR REPLACE PROCEDURE del_orders_between(low_id INT, high_id INT)
LANGUAGE PLPGSQL
AS $$
BEGIN
	FOR i IN low_id..high_id LOOP
		DELETE FROM orders CASCADE
		WHERE order_id = i;
	END LOOP;
	COMMIT;
END;
$$;

SELECT * FROM orders LIMIT 50;
CALL del_orders_between(5, 45);
DROP PROCEDURE del_orders_between;
