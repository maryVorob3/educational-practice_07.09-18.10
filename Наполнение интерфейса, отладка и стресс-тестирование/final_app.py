import tkinter as tk
from tkinter import ttk


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


def fetch_partners_from_backend():
    raw_dataset = [
        (1, "ЗАО", "База Строитель", "Иванова Светлана Сергеевна", "+7 223 322 22 32", 10, 155000),
        (2, "ООО", "Паркет 29", "Петров Петр Петрович", "+7 921 555 44 33", 10, 45000),
        (3, "ПАО", "Стройкомплект", "Сидоров Алексей Владимирович", "+7 905 111 22 33", 10, 320000),
        (4, "ОАО", "Ремонт и Точка", "Кузнецов Андрей Николаевич", "+7 812 444 55 66", 8, 0),
        (5, "ООО", "Новый Партнер Без Продаж", "Смирнова Ольга Игоревна", "+7 999 000 11 22", 5, None),
    ]

    clean_partners = []
    for item in raw_dataset:
        sales = item[6]
        discount_val = calculate_partner_discount(sales)
        clean_partners.append({
            "id": item[0],
            "type": item[1],
            "name": item[2],
            "director": item[3],
            "phone": item[4],
            "rating": item[5],
            "total_sales": 0 if sales is None else sales,
            "discount": discount_val
        })
    return clean_partners


class FinalPartnerApp(tk.Tk):
    def __init__(self, partners_list):
        super().__init__()
        self.title("CRM: Список партнеров и скидок")
        self.geometry("780x620")
        self.configure(bg="#F4F4F4")

        header = tk.Frame(self, bg="#FFFFFF", pady=15, padx=20)
        header.pack(fill="x", side="top")

        tk.Label(
            header,
            text="Список партнеров компании",
            font=("Segoe UI", 16, "bold"),
            bg="#FFFFFF",
            fg="#222222"
        ).pack(side="left")

        container = tk.Frame(self, bg="#F4F4F4")
        container.pack(fill="both", expand=True, padx=20, pady=10)

        canvas = tk.Canvas(container, bg="#F4F4F4", highlightthickness=0)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg="#F4F4F4")

        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scroll_frame, anchor="nw", width=720)
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        for p in partners_list:
            self.create_card(scroll_frame, p)

    def create_card(self, parent, data):
        card = tk.Frame(parent, bg="#FFFFFF", bd=1, relief="solid", padx=16, pady=12)
        card.pack(fill="x", pady=6)

        top_line = tk.Frame(card, bg="#FFFFFF")
        top_line.pack(fill="x")

        title_text = f"{data['type']} | {data['name']}"
        tk.Label(top_line, text=title_text, font=("Segoe UI", 12, "bold"), bg="#FFFFFF", fg="#111111").pack(side="left")
        tk.Label(top_line, text=f"{data['discount']}%", font=("Segoe UI", 12, "bold"), bg="#FFFFFF", fg="#111111").pack(side="right")

        tk.Label(card, text=f"Директор: {data['director']}", font=("Segoe UI", 10), bg="#FFFFFF", fg="#444444", anchor="w").pack(fill="x", pady=(4, 1))
        tk.Label(card, text=f"{data['phone']}", font=("Segoe UI", 10), bg="#FFFFFF", fg="#444444", anchor="w").pack(fill="x", pady=1)
        tk.Label(card, text=f"Рейтинг: {data['rating']}", font=("Segoe UI", 10), bg="#FFFFFF", fg="#444444", anchor="w").pack(fill="x", pady=1)


def run_final_demo_tests():
    assert calculate_partner_discount(None) == 0
    assert calculate_partner_discount(0) == 0
    assert calculate_partner_discount(9999) == 0
    assert calculate_partner_discount(10000) == 5
    assert calculate_partner_discount(50000) == 10
    assert calculate_partner_discount(300000) == 15

    partners = fetch_partners_from_backend()
    assert len(partners) == 5
    assert partners[3]["discount"] == 0
    assert partners[4]["discount"] == 0
    print("Final tests and resilience verification: SUCCESS")


if __name__ == "__main__":
    run_final_demo_tests()
    data = fetch_partners_from_backend()
    app = FinalPartnerApp(data)
    app.mainloop()
