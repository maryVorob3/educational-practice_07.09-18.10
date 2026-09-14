def calculate_partner_discount(total_quantity: int) -> int:
    if total_quantity is None:
        return 0
    if not isinstance(total_quantity, (int, float)) or total_quantity < 0:
        return 0

    quantity = int(total_quantity)
    if quantity < 10000:
        return 0
    elif 10000 <= quantity < 50000:
        return 5
    elif 50000 <= quantity < 300000:
        return 10
    else:
        return 15


def get_partners_data(cursor=None):
    if cursor is not None:
        query = """
        SELECT 
            p.id,
            pt.type_name,
            p.name,
            p.director_name,
            p.phone,
            p.rating,
            COALESCE(SUM(ps.quantity), 0) AS total_sales
        FROM partners p
        JOIN partner_types pt ON p.type_id = pt.id
        LEFT JOIN partner_sales ps ON p.id = ps.partner_id
        GROUP BY p.id, pt.type_name, p.name, p.director_name, p.phone, p.rating
        ORDER BY p.id;
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        result = []
        for r in rows:
            sales = r[6] if r[6] is not None else 0
            result.append({
                "id": r[0],
                "type": r[1],
                "name": r[2],
                "director": r[3],
                "phone": r[4],
                "rating": r[5],
                "total_sales": sales,
                "discount": calculate_partner_discount(sales)
            })
        return result

    mock_db_rows = [
        (1, "ЗАО", "База Строитель", "Иванова Светлана Сергеевна", "+7 223 322 22 32", 10, 155000),
        (2, "ООО", "Паркет 29", "Петров Петр Петрович", "+7 921 555 44 33", 10, 45000),
        (3, "ПАО", "Стройкомплект", "Сидоров Алексей Владимирович", "+7 905 111 22 33", 10, 320000),
        (4, "ОАО", "Ремонтник", "Кузнецов Андрей Николаевич", "+7 812 444 55 66", 8, 0),
        (5, "ООО", "Новый Партнер", "Смирнова Ольга Игоревна", "+7 999 000 11 22", 5, None)
    ]

    partners = []
    for r in mock_db_rows:
        sales = r[6] if r[6] is not None else 0
        partners.append({
            "id": r[0],
            "type": r[1],
            "name": r[2],
            "director": r[3],
            "phone": r[4],
            "rating": r[5],
            "total_sales": sales,
            "discount": calculate_partner_discount(sales)
        })
    return partners


if __name__ == "__main__":
    data = get_partners_data()
    print(f"Processed partners: {len(data)}")
    for p in data:
        print(f"{p['type']} | {p['name']} | Sales: {p['total_sales']} | Discount: {p['discount']}%")
