TRUNCATE partner_sales, partners, partner_types, products RESTART IDENTITY CASCADE;

INSERT INTO partner_types (type_name) VALUES 
('ЗАО'), ('ООО'), ('ПАО'), ('ОАО')
ON CONFLICT (type_name) DO NOTHING;

CREATE TEMP TABLE staging_partners (
    type_name VARCHAR(50),
    name VARCHAR(255),
    director_name VARCHAR(255),
    email VARCHAR(100),
    phone VARCHAR(30),
    legal_address TEXT,
    inn VARCHAR(12),
    rating INT
);

CREATE TEMP TABLE staging_sales (
    partner_name VARCHAR(255),
    product_article VARCHAR(50),
    quantity INT,
    sale_date DATE
);

COPY staging_partners FROM 'import_partners.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',');
COPY staging_sales FROM 'import_sales.txt' WITH (FORMAT csv, HEADER false, DELIMITER '\t');

DELETE FROM staging_partners 
WHERE name IS NULL 
   OR inn IS NULL 
   OR LENGTH(inn) NOT IN (10, 12);

DELETE FROM staging_sales 
WHERE quantity <= 0 
   OR sale_date > CURRENT_DATE;

INSERT INTO partners (type_id, name, director_name, email, phone, legal_address, inn, rating)
SELECT DISTINCT ON (sp.inn)
    pt.id,
    sp.name,
    sp.director_name,
    sp.email,
    sp.phone,
    sp.legal_address,
    sp.inn,
    COALESCE(sp.rating, 0)
FROM staging_partners sp
JOIN partner_types pt ON sp.type_name = pt.type_name
ON CONFLICT (inn) DO NOTHING;

INSERT INTO partner_sales (partner_id, product_id, quantity, sale_date)
SELECT 
    p.id,
    pr.id,
    ss.quantity,
    ss.sale_date
FROM staging_sales ss
JOIN partners p ON ss.partner_name = p.name
JOIN products pr ON ss.product_article = pr.article;

SELECT COUNT(*) AS total_partner_types FROM partner_types;
SELECT COUNT(*) AS total_partners FROM partners;
SELECT COUNT(*) AS total_products FROM products;
SELECT COUNT(*) AS total_partner_sales FROM partner_sales;
