-- SQL script to insert sample data
insert into customers (name, email, join_date) values
('John', 'john@example.com', '2023-01-15'),
('tobi', 'mary@example.com', '2022-11-20'),
('patrick', 'alice@example.com', '2022-07-05'),
('clinton', 'bob@example.com', '2023-03-10'),
('celine', 'eve@example.com', '2023-04-25'),
('billie', 'tom@example.com', '2022-08-12'),
('eilish', 'lara@example.com', '2023-06-01'),
('taylor', 'mike@example.com', '2023-02-14'),
('swift', 'sara@example.com', '2022-09-30'),
('flash', 'paul@example.com', '2023-05-18');

insert into products (product_name, category, price) values
('Apple juice', 'Drinks', 700),
('ogbono', 'vegetable', 4300),
('tuwo', 'food', 5330),
('eba', 'food', 8000),
('turkey', 'Meat', 5000),
('fish', 'fish', 7000),
('paper', 'writing', 1200),
('sweet', 'Dairy', 3500),
('chivita', 'Drinks', 2000),
('Eggs', 'poultry', 2500);

insert into orders (customer_id, product_id, quantity, order_date) values
(1, 1, 5, '2023-02-01'),
(2, 3, 2, '2023-03-15'),
(3, 2, 1, '2023-04-10'),
(4, 5, 4, '2023-05-20'),
(5, 4, 3, '2023-06-05'),
(6, 6, 2, '2023-01-25'),
(7, 8, 1, '2023-02-18'),
(8, 2, 6, '2023-03-30'),
(9, 9, 2, '2023-04-22'),
(10, 10, 5, '2023-05-12');