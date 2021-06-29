-- first (show customer city and chosen brand)
EXPLAIN(ANALYSE) 
SELECT o.order_id, c.customer_id, ca.brand chosen_brand, a.city customer_city
FROM orders o
JOIN customer c USING (customer_id)
JOIN car ca USING (car_id)
JOIN address_telephone a ON c.info_id = a.at_id;

CREATE INDEX idx_city ON address_telephone(city);
CREATE INDEX idx_cust_id ON orders(customer_id);
CREATE INDEX idx_car_model ON car(model);

DROP INDEX idx_city;
DROP INDEX idx_cust_id;
DROP INDEX idx_car_model;


-- second (certain number of the car)
EXPLAIN(ANALYSE)
SELECT o.order_id, c.customer_id, ca.brand, ca.model, ca.number
FROM orders o
JOIN customer c USING (customer_id)
JOIN car ca USING (car_id)
WHERE ca.number = 'number#44';

CREATE INDEX idx_car_number ON car(number);
DROP INDEX idx_car_number;

-- third (shows total spent for orders with renting days < 4)
EXPLAIN(ANALYSE)
SELECT o.order_id, 
	   	o.renting_days, 
		c.customer_id, 
		ca.price, 
		ca.price * o.renting_days total_spent, 
		o.renting_date
FROM orders o
JOIN customer c USING (customer_id)
JOIN car ca USING (car_id)
WHERE o.renting_days < 4 AND o.renting_date BETWEEN '2021-08-02' AND '2021-09-30';

CREATE INDEX idx_renting_days ON orders USING btree(renting_days);
CREATE INDEX idx_renting_date ON orders USING btree(renting_date);
DROP INDEX idx_renting_days;
DROP INDEX idx_renting_date;

SET enable_seqscan = OFF;
SET enable_seqscan = ON;
