CREATE TABLE customers (
	customer_id CHAR(32),
	customer_unique_id CHAR(32),
	zip_code INTEGER,
	city VARCHAR,
	state_code CHAR(2)
);

CREATE TABLE order_payments (
	order_id CHAR(32),
	payment_sequential SMALLINT,
	payment_type VARCHAR(11) CHECK (payment_type IN ('credit_card', 'boleto', 'voucher', 'debit_card', 'not_defined')),
	payment_installments SMALLINT,
	payment_value REAL
);

CREATE TABLE products(
	product_id CHAR(32),
	product_category_name VARCHAR,
	product_name_lenght INTEGER,
	product_description_lenght INTEGER,
	product_photos_qty INTEGER,
	product_weight_g INTEGER,
	product_length_cm INTEGER,
	product_height_cm INTEGER,
	product_width_cm INTEGER
);

CREATE TABLE orders (
	order_id CHAR(32),
	customer_id CHAR(32),
	order_status VARCHAR CHECK(order_status IN ('delivered', 'invoiced', 'shipped', 'processing', 'unavailable',
       'canceled', 'created', 'approved')),
	order_purchase_timestamp TIMESTAMP,
	order_approved_at TIMESTAMP,
	order_delivered_carrier_date TIMESTAMP,
	order_delivered_customer_date TIMESTAMP,
	order_estimated_delivery_date TIMESTAMP
);

CREATE TABLE product_category_name_translation(
	product_category_name VARCHAR,
	product_category_name_english VARCHAR
);

CREATE TABLE order_items(
	order_id CHAR(32),
	order_item_id SMALLINT,
	product_id	CHAR(32),
	seller_id CHAR(32),
	shipping_limit_date TIMESTAMP,
 	price REAL,
	freight_value REAL
);

CREATE TABLE reviews(
	review_id CHAR(32),
	order_id CHAR(32),
	review_score SMALLINT CHECK(review_score BETWEEN 1 AND 5),
	review_comment_title VARCHAR,
	review_comment_message VARCHAR,
	review_creation_date DATE,
	review_answer_timestamp TIMESTAMP
);

CREATE TABLE sellers(
	seller_id CHAR(32),
	seller_zip_code_prefix SMALLINT,
	seller_city VARCHAR,
	seller_state CHAR(2)
);

CREATE TABLE geo_location(
	geolocation_zip_code_prefix SMALLINT,
	geolocation_lat	REAL,
	geolocation_lng REAL,
	geolocation_city VARCHAR,
	geolocation_state CHAR(2)
);