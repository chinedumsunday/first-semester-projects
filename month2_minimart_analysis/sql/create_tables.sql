-- SQL script to create necessary tables
CREATE TABLE IF NOT EXISTS customers (
    customer_id serial primary key,
    name varchar(10),
    email varchar(256),
    join_date date
);

CREATE TABLE IF NOT EXISTS products (
    product_id serial primary key,
    product_name varchar(10),
    category varchar(10)
    price numeric
);

CREATE TABLE IF NOT EXISTS orders (
    order_id serial primary key,
    customer_id int references customers(customer_id),
    product_id int references products(product_id),
    quantity int,
    order_date date
);

