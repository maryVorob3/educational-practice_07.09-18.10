-- 1. Список всех партнеров с общим объемом продаж
SELECT 
    p.id,
    pt.type_name AS partner_type,
    p.name AS partner_name,
    p.director_name,
    p.phone,
    p.rating,
    COALESCE(SUM(ps.quantity), 0) AS total_sales_volume
FROM partners p
JOIN partner_types pt ON p.type_id = pt.id
LEFT JOIN partner_sales ps ON p.id = ps.partner_id
GROUP BY p.id, pt.type_name, p.name, p.director_name, p.phone, p.rating
ORDER BY p.name;

-- 2. Редактирование данных партнера
UPDATE partners
SET 
    name = 'ООО Паркет-Мастер',
    director_name = 'Иванов Иван Иванович',
    email = 'info@parketmaster.ru',
    phone = '+7 999 111-22-33',
    rating = 15
WHERE id = 1;

-- 3. История отгрузок конкретного партнера
SELECT 
    ps.id AS sale_id,
    prod.name AS product_name,
    ps.quantity,
    ps.sale_date,
    (ps.quantity * prod.min_cost) AS estimated_total_cost
FROM partner_sales ps
JOIN products prod ON ps.product_id = prod.id
WHERE ps.partner_id = 1
ORDER BY ps.sale_date DESC;
