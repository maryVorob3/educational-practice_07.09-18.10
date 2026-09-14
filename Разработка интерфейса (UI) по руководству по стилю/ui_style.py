import tkinter as tk

PARTNERS_SAMPLE = [
    {
        "type": "Тип",
        "name": "Наименование партнера",
        "director": "Директор",
        "phone": "+7 223 322 22 32",
        "rating": 10,
        "discount": 10
    },
    {
        "type": "Тип",
        "name": "Наименование партнера",
        "director": "Директор",
        "phone": "+7 223 322 22 32",
        "rating": 10,
        "discount": 10
    },
    {
        "type": "Тип",
        "name": "Наименование партнера",
        "director": "Директор",
        "phone": "+7 223 322 22 32",
        "rating": 10,
        "discount": 10
    }
]

class PartnerStyleApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CRM: Список партнеров и скидок")
        self.geometry("780x620")
        self.configure(bg="#EFEFEF")

        header_frame = tk.Frame(self, bg="#FFFFFF", padx=20, pady=15)
        header_frame.pack(fill="x", side="top")

        title_lbl = tk.Label(
            header_frame,
            text="Партнеры компании",
            font=("Segoe UI", 16, "bold"),
            bg="#FFFFFF",
            fg="#1A1A1A"
        )
        title_lbl.pack(side="left")

        container = tk.Frame(self, bg="#EFEFEF", padx=25, pady=15)
        container.pack(fill="both", expand=True)

        for p in PARTNERS_SAMPLE:
            self.draw_card(container, p)

    def draw_card(self, parent, data):
        card = tk.Frame(parent, bg="#FFFFFF", bd=1, relief="solid", padx=16, pady=12)
        card.pack(fill="x", pady=6)

        top_line = tk.Frame(card, bg="#FFFFFF")
        top_line.pack(fill="x")

        title = f"{data['type']} | {data['name']}"
        tk.Label(top_line, text=title, font=("Segoe UI", 12, "bold"), bg="#FFFFFF", fg="#000000").pack(side="left")
        tk.Label(top_line, text=f"{data['discount']}%", font=("Segoe UI", 12, "bold"), bg="#FFFFFF", fg="#000000").pack(side="right")

        tk.Label(card, text=f"Директор: {data['director']}", font=("Segoe UI", 10), bg="#FFFFFF", fg="#444444", anchor="w").pack(fill="x", pady=(4, 1))
        tk.Label(card, text=f"{data['phone']}", font=("Segoe UI", 10), bg="#FFFFFF", fg="#444444", anchor="w").pack(fill="x", pady=1)
        tk.Label(card, text=f"Рейтинг: {data['rating']}", font=("Segoe UI", 10), bg="#FFFFFF", fg="#444444", anchor="w").pack(fill="x", pady=1)


if __name__ == "__main__":
    app = PartnerStyleApp()
    app.mainloop()
