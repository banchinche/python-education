CREATE TABLE IF NOT EXISTS categories (
	category_id INT PRIMARY KEY,
	category_title VARCHAR(255),
	category_description TEXT
);


CREATE TABLE IF NOT EXISTS products (
	product_id INT PRIMARY KEY,
	product_title VARCHAR(255),
	product_description TEXT,
	in_stock INT,
	price REAL,
	slug VARCHAR(45),
	category_id INT,
	FOREIGN KEY (category_id)
		REFERENCES categories(category_id)
);


CREATE TABLE IF NOT EXISTS users (
	user_id INT PRIMARY KEY,
	email VARCHAR(255),
	password VARCHAR(255),
	first_name VARCHAR(255),
	last_name VARCHAR(255),
	middle_name VARCHAR(255),
	is_staff SMALLINT,
	country VARCHAR(255),
	city VARCHAR(255),
	address TEXT
);


CREATE TABLE IF NOT EXISTS carts (
	cart_id INT PRIMARY KEY,
	user_id INT,
	subtotal DECIMAL,
	total DECIMAL,
	timestamp TIMESTAMP(2),
	FOREIGN KEY (user_id)
		REFERENCES users(user_id)
);


CREATE TABLE IF NOT EXISTS cart_product (
	cart_id INT,
	product_id INT,
    FOREIGN KEY (cart_id)
         REFERENCES carts(cart_id),
     FOREIGN KEY (product_id)
         REFERENCES products(product_id)

);


CREATE TABLE IF NOT EXISTS order_status (
	order_status_id INT PRIMARY KEY,
	status_name VARCHAR(255)
);


CREATE TABLE IF NOT EXISTS orders (
	order_id INT PRIMARY KEY,
	cart_id INT,
	order_status_id INT,
	shipping_total DECIMAL,
	total DECIMAL,
	created_at TIMESTAMP(2),
	updated_at TIMESTAMP(2),
	FOREIGN KEY (cart_id)
		REFERENCES carts(cart_id),
	FOREIGN KEY (order_status_id)
		REFERENCES order_status(order_status_id)
);
