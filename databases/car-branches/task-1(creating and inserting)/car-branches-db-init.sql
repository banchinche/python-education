-- INITIALIZING DATABASE

CREATE DATABASE car_branches;

-- USEFUL FUNCTIONS FOR INSERTING...
CREATE OR REPLACE FUNCTION random_between(low INT, high INT) 
RETURNS INT
LANGUAGE PLPGSQL
AS $$
BEGIN
   RETURN floor(random()* (high-low + 1) + low);
END;
$$;

CREATE OR REPLACE FUNCTION random_date()
RETURNS TIMESTAMP
LANGUAGE PLPGSQL
AS $$
BEGIN
	SET datestyle TO DMY, SQL;
	RETURN date_trunc('day', NOW() + (random() * (interval '90 days')) + '30 days');
END;
$$;

-- CHECKING WORKING...

SELECT random_date();
SELECT random_between(1, 5);


-- CREATING TABLES...

CREATE TABLE IF NOT EXISTS  address_telephone (
	at_id SERIAL PRIMARY KEY,
	city VARCHAR,
	street VARCHAR,
	house INT,
	telephone VARCHAR
);

CREATE TABLE IF NOT EXISTS customer (
	customer_id SERIAL PRIMARY KEY,
	info_id INT NOT NULL,
	first_name VARCHAR,
	last_name VARCHAR,
	FOREIGN KEY (info_id)
 		REFERENCES address_telephone(at_id)
);

CREATE TABLE IF NOT EXISTS branch (
	branch_id SERIAL PRIMARY KEY,
	info_id INT NOT NULL,
	number INT NOT NULL,
	FOREIGN KEY (info_id)
		REFERENCES address_telephone(at_id)
);

CREATE TABLE IF NOT EXISTS car (
	car_id SERIAL PRIMARY KEY,
	branch_id INT NOT NULL,
	brand VARCHAR NOT NULL,
	model VARCHAR NOT NULL,
	number VARCHAR NOT NULL,
	price MONEY NOT NULL,
	FOREIGN KEY (branch_id)
 		REFERENCES branch(branch_id)
);

CREATE TABLE IF NOT EXISTS orders (
	order_id SERIAL PRIMARY KEY,
	customer_id INT NOT NULL,
	car_id INT NOT NULL,
	renting_days INT NOT NULL,
	renting_date TIMESTAMP(6) NOT NULL,
	FOREIGN KEY (customer_id)
 		REFERENCES customer(customer_id),
	FOREIGN KEY (car_id)
 		REFERENCES car(car_id)
);


-- INSERTING DATA
CREATE OR REPLACE PROCEDURE inserting_address_phone(rows_count INT)
LANGUAGE PLPGSQL
AS $$
DECLARE
	temp_city VARCHAR := '';
	temp_street VARCHAR := '';
	temp_phone VARCHAR := '';
BEGIN
	FOR i IN 1..rows_count LOOP
		temp_city := 'city' || CAST(i AS VARCHAR);
		temp_street := 'street' || CAST(i AS VARCHAR);
		temp_phone := 'phone' || CAST(i AS VARCHAR);
		INSERT INTO address_telephone(city, street, house, telephone) 
		VALUES (temp_city, temp_street, i, temp_phone);
	END LOOP;
	COMMIT;
END;
$$;


CREATE OR REPLACE PROCEDURE inserting_customer(rows_count INT)
LANGUAGE PLPGSQL
AS $$
DECLARE
	count_addresses INT;
	temp_name VARCHAR := '';
	temp_surname VARCHAR := '';
BEGIN
	SELECT COUNT(*) INTO count_addresses FROM address_telephone;
	IF rows_count <= (count_addresses / 2) THEN
		FOR i IN 1..rows_count LOOP
			temp_name := 'first-name' || CAST(i AS VARCHAR);
			temp_surname := 'last-name' || CAST(i AS VARCHAR);
			INSERT INTO customer(info_id, first_name, last_name) 
			VALUES (i, temp_name, temp_surname);
		END LOOP;
	ELSE
		RAISE EXCEPTION 'Dublicate addresses possible!';
	END IF;
	COMMIT;
END;
$$;

CREATE OR REPLACE PROCEDURE inserting_branch(rows_count INT)
LANGUAGE PLPGSQL
AS $$
DECLARE
	count_addresses INT;
	second_part_addresses INT;
BEGIN
	SELECT COUNT(*) INTO count_addresses FROM address_telephone;
	second_part_addresses := count_addresses / 2 + 1;
	IF rows_count <= (count_addresses / 2) THEN
		FOR i IN second_part_addresses..(second_part_addresses + rows_count - 1) LOOP
			INSERT INTO branch(info_id, number) 
			VALUES (i, i - second_part_addresses + 1);
		END LOOP;
	ELSE
		RAISE EXCEPTION 'Dublicate addresses possible!';
	END IF;
	COMMIT;
END;
$$;


CREATE OR REPLACE PROCEDURE inserting_car(rows_count INT)
LANGUAGE PLPGSQL
AS $$
DECLARE
	branches_count INT;
	temp_price MONEY;
	counter INT := 0;
	temp_brand VARCHAR := '';
	temp_model VARCHAR := '';
	temp_number VARCHAR := '';
	
BEGIN
	SELECT COUNT(*) INTO branches_count FROM branch;
	<<f_loop>>
	LOOP
		FOR i IN 1..branches_count LOOP
			counter := counter + 1;
			EXIT f_loop WHEN counter = rows_count + 1;
			temp_price := CAST((i * 100) AS MONEY);
			temp_brand := 'brand' || CAST(i AS VARCHAR);
			temp_model := 'model' || CAST(i AS VARCHAR);
			temp_number := 'number#' || CAST(i AS VARCHAR);
			INSERT INTO car(branch_id, brand, model, number, price)
			VALUES (i, temp_brand, temp_model, temp_number, temp_price);
		END LOOP;
	END LOOP;
	COMMIT;
END;
$$;


CREATE OR REPLACE PROCEDURE inserting_orders(rows_count INT)
LANGUAGE PLPGSQL
AS $$
DECLARE
	car_count INT;
	temp_customer INT;
	temp_branch INT;
	temp_car INT;
	temp_days INT;
	temp_date TIMESTAMP;
BEGIN
	SELECT COUNT(*) INTO car_count FROM car;
	FOR i IN 1..car_count LOOP
		INSERT INTO orders(customer_id, car_id, renting_days, renting_date)
		VALUES (i, i, random_between(1, 6), random_date());
	END LOOP;
	COMMIT;
END;
$$;

-- DROPS
DROP TABLE address_telephone CASCADE;
DROP TABLE branch CASCADE;
DROP TABLE car CASCADE;
DROP TABLE orders CASCADE;
DROP TABLE customer CASCADE;

DROP PROCEDURE inserting_address_phone(integer);
DROP PROCEDURE inserting_customer(integer);
DROP PROCEDURE inserting_branch(integer);
DROP PROCEDURE inserting_car(integer);
DROP PROCEDURE inserting_orders(integer);


-- CALLS
CALL inserting_address_phone(500);
CALL inserting_customer(200);
CALL inserting_branch(200);
CALL inserting_car(100);
CALL inserting_orders(100);

-- CHECKING TABLES
SELECT * FROM address_telephone;
SELECT * FROM customer;
SELECT * FROM branch;
SELECT * FROM car;
SELECT * FROM orders;
