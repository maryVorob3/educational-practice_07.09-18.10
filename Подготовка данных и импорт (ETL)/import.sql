TRUNCATE partner_sales, partners, partner_types, products RESTART IDENTITY CASCADE;

INSERT INTO partner_types (type_name) VALUES 
('ЗАО'), ('ООО'), ('ПАО'), ('ОАО');
