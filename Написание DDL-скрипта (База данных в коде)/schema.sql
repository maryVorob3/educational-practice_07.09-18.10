CREATE TABLE partner_types (
    id SERIAL PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE partners (
    id SERIAL PRIMARY KEY,
    type_id INT NOT NULL REFERENCES partner_types(id),
    name VARCHAR(255) NOT NULL,
    director_name VARCHAR(255),
    email VARCHAR(100),
    phone VARCHAR(30),
    legal_address TEXT,
    inn VARCHAR(12) UNIQUE,
    rating INT DEFAULT 0
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    article VARCHAR(50) UNIQUE,
    min_cost DECIMAL(10, 2) NOT NULL DEFAULT 0.00
);

CREATE TABLE partner_sales (
    id SERIAL PRIMARY KEY,
    partner_id INT NOT NULL REFERENCES partners(id) ON DELETE CASCADE,
    product_id INT NOT NULL REFERENCES products(id),
    quantity INT NOT NULL CHECK (quantity > 0),
    sale_date DATE NOT NULL DEFAULT CURRENT_DATE
);
