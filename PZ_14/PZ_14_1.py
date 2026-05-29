# Задание 1. В соответствии с номером варианта перейти по ссылке на прототип. Реализовать его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально приближенный к оригиналу (см. таблицу 1).

import tkinter as tk
from tkinter import ttk, messagebox

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    message = message_text.get("1.0", tk.END).strip()
    
    if not name or not email:
        messagebox.showwarning("Ошибка", "Заполните обязательные поля!")
        return
    
    messagebox.showinfo("Успешно", f"Форма отправлена!\n\nИмя: {name}\nEmail: {email}\nТелефон: {phone}\n\nСообщение:\n{message}")

root = tk.Tk()
root.title("Contact Form")
root.geometry("500x550")
root.resizable(False, False)

# Заголовок
title_label = tk.Label(root, text="SUBMIT FORM", font=("Arial", 18, "bold"))
title_label.pack(pady=20)

# Поля
tk.Label(root, text="Name *", font=("Arial", 10)).pack(anchor="w", padx=50)
name_entry = tk.Entry(root, width=40)
name_entry.pack(pady=5)

tk.Label(root, text="Email *", font=("Arial", 10)).pack(anchor="w", padx=50)
email_entry = tk.Entry(root, width=40)
email_entry.pack(pady=5)

tk.Label(root, text="Phone", font=("Arial", 10)).pack(anchor="w", padx=50)
phone_entry = tk.Entry(root, width=40)
phone_entry.pack(pady=5)

tk.Label(root, text="Message", font=("Arial", 10)).pack(anchor="w", padx=50)
message_text = tk.Text(root, width=40, height=8)
message_text.pack(pady=5)

# Кнопка
submit_btn = tk.Button(root, text="SUBMIT", font=("Arial", 12, "bold"), 
                      bg="#4CAF50", fg="white", width=15, command=submit_form)
submit_btn.pack(pady=20)

root.mainloop()