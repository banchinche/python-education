CREATE OR REPLACE FUNCTION check_changing_car_price()
RETURNS TRIGGER
LANGUAGE PLPGSQL
AS $$
DECLARE low_limit MONEY DEFAULT 100;
BEGIN

	IF NEW.price < low_limit then
		RAISE 'Minimal renting price is 100$!';
	END IF;
RETURN NEW;
END;
$$;
	
CREATE TRIGGER check_price_car
	BEFORE INSERT OR UPDATE
   	ON car
	FOR EACH ROW
   	EXECUTE PROCEDURE check_changing_car_price();

DROP TRIGGER check_price_car ON car;
DROP FUNCTION check_changing_car_price();
SELECT * FROM car WHERE car_id = 20;
UPDATE car
SET price = 1200
WHERE car_id = 20;

UPDATE car
SET price = 99
WHERE car_id = 20;

CREATE OR REPLACE FUNCTION check_car_number()
RETURNS TRIGGER
LANGUAGE PLPGSQL
AS $$
BEGIN
	IF NEW.number LIKE 'number#%' THEN
		RETURN NEW;
	ELSE
		RAISE EXCEPTION 'Number does not follow pattern!';
	END IF;
END;
$$;

CREATE TRIGGER check_number
	AFTER INSERT OR UPDATE
	ON car
	FOR EACH ROW
	EXECUTE PROCEDURE check_car_number();

BEGIN;
SELECT * FROM car WHERE car_id = 3;
UPDATE car
SET number = 'number#999'
ROLLBACK;
WHERe car_id = 3;