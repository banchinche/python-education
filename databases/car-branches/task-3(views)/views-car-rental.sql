CREATE OR REPLACE VIEW branch_info AS
	SELECT branch_id, number, a.city, a.street, a.house, a.telephone
	FROM branch b
	JOIN address_telephone a ON b.info_id = a.at_id;

DROP VIEW branch_info;
SELECT * FROM branch_info;


CREATE OR REPLACE VIEW customer_info AS
	SELECT customer_id, first_name, last_name, a.city, a.street, a.house, a.telephone
	FROM customer c
	JOIN address_telephone a ON c.info_id = a.at_id;

DROP VIEW customer_info;
SELECT * FROM customer_info;


CREATE MATERIALIZED VIEW total_spent_many_days_september AS
	SELECT o.order_id, 
			o.renting_days, 
			c.customer_id, 
			ca.price, 
			ca.price * o.renting_days total_spent, 
			o.renting_date
	FROM orders o
	JOIN customer c USING (customer_id)
	JOIN car ca USING (car_id)
	WHERE o.renting_days > 4 AND o.renting_date BETWEEN '2021-09-01' AND '2021-09-30';

SELECT * FROM total_spent_many_days_september;
DROP MATERIALIZED VIEW total_spent_many_days_september;


