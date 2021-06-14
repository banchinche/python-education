COPY categories FROM '/usr/src/source_data/categories.csv' DELIMITER ',';

COPY products FROM '/usr/src/source_data/products.csv' DELIMITER ',';


COPY users FROM '/usr/src/source_data/users.csv' DELIMITER ',';


COPY carts FROM '/usr/src/source_data/carts.csv' DELIMITER ',';

COPY cart_product FROM '/usr/src/source_data/cart_products.csv' DELIMITER ',';


COPY order_status FROM '/usr/src/source_data/order_statuses.csv' DELIMITER ',';


COPY orders FROM '/usr/src/source_data/orders.csv' DELIMITER ',';
