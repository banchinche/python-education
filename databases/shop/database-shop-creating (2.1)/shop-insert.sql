COPY categories(category_id, category_title, category_description)
FROM '/usr/src/source_data/categories.csv'
DELIMITER ',';

COPY products(product_id, product_title, product_description, in_stock, price, slug, category_id)
FROM '/usr/src/source_data/products.csv'
DELIMITER ',';


COPY users(user_id, email, password, first_name, last_name, middle_name, is_staff, country, city, address)
FROM '/usr/src/source_data/users.csv'
DELIMITER ',';


COPY carts(cart_id, user_id, subtotal, total, timestamp)
FROM '/usr/src/source_data/carts.csv'
DELIMITER ',';

COPY cart_product(cart_id, product_id)
FROM '/usr/src/source_data/cart_products.csv'
DELIMITER ',';


COPY order_status(order_status_id, status_name)
FROM '/usr/src/source_data/order_statuses.csv'
DELIMITER ',';


COPY orders(order_id, cart_id, order_status_id, shipping_total, total, created_at, updated_at)
FROM '/usr/src/source_data/orders.csv'
DELIMITER ',';
