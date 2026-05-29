import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

conn = sqlite3.connect('pharmacy.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS medicines (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    usage TEXT,
    quantity INTEGER,
    price REAL,
    country TEXT
)''')
conn.commit()

def add_medicine():
    try:
        cur.execute("INSERT INTO medicines (name, usage, quantity, price, country) VALUES (?, ?, ?, ?, ?)",
                    (name_entry.get(), usage_entry.get(), int(quantity_entry.get()),
                     float(price_entry.get()), country_entry.get()))
        conn.commit()
        messagebox.showinfo("Успешно", "Лекарство добавлено")
        clear_fields()
        show_all()
    except Exception as e:
        messagebox.showerror("Ошибка", str(e))

def show_all():
    for row in tree.get_children():
        tree.delete(row)
    cur.execute("SELECT * FROM medicines")
    for row in cur.fetchall():
        tree.insert("", tk.END, values=row)

def search_medicine():
    for row in tree.get_children():
        tree.delete(row)
    query = search_entry.get()
    cur.execute("""SELECT * FROM medicines WHERE 
                   name LIKE ? OR usage LIKE ? OR country LIKE ?""",
                (f'%{query}%', f'%{query}%', f'%{query}%'))
    for row in cur.fetchall():
        tree.insert("", tk.END, values=row)

def delete_medicine():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Внимание", "Выберите запись для удаления")
        return
    if messagebox.askyesno("Подтверждение", "Удалить выбранное лекарство?"):
        mid = tree.item(selected[0])['values'][0]
        cur.execute("DELETE FROM medicines WHERE id=?", (mid,))
        conn.commit()
        show_all()

def update_medicine():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Внимание", "Выберите запись для редактирования")
        return
    mid = tree.item(selected[0])['values'][0]
    try:
        cur.execute("""UPDATE medicines SET name=?, usage=?, quantity=?, 
                       price=?, country=? WHERE id=?""",
                    (name_entry.get(), usage_entry.get(), int(quantity_entry.get()),
                     float(price_entry.get()), country_entry.get(), mid))
        conn.commit()
        messagebox.showinfo("Успешно", "Данные обновлены")
        show_all()
    except Exception as e:
        messagebox.showerror("Ошибка", str(e))

def clear_fields():
    name_entry.delete(0, tk.END)
    usage_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    country_entry.delete(0, tk.END)

#GUI
root = tk.Tk()
root.title("Аптека — Управление лекарствами")
root.geometry("1000x600")

# Поля ввода
tk.Label(root, text="Название препарата:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Применение:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
usage_entry = tk.Entry(root, width=30)
usage_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Количество:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
quantity_entry = tk.Entry(root, width=30)
quantity_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Цена:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
price_entry = tk.Entry(root, width=30)
price_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Страна-производитель:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
country_entry = tk.Entry(root, width=30)
country_entry.grid(row=4, column=1, padx=10, pady=5)

# Кнопки
btn_frame = tk.Frame(root)
btn_frame.grid(row=5, column=0, columnspan=2, pady=10)

tk.Button(btn_frame, text="Добавить", bg="#4CAF50", fg="white", command=add_medicine).pack(side="left", padx=5)
tk.Button(btn_frame, text="Обновить", bg="#2196F3", fg="white", command=update_medicine).pack(side="left", padx=5)
tk.Button(btn_frame, text="Удалить", bg="#f44336", fg="white", command=delete_medicine).pack(side="left", padx=5)
tk.Button(btn_frame, text="Очистить поля", command=clear_fields).pack(side="left", padx=5)

# Поиск
tk.Label(root, text="Поиск:").grid(row=6, column=0, padx=10, pady=5, sticky="w")
search_entry = tk.Entry(root, width=30)
search_entry.grid(row=6, column=1, padx=10, pady=5, sticky="w")
tk.Button(root, text="Найти", command=search_medicine).grid(row=6, column=1, padx=150, pady=5, sticky="e")

# Таблица
columns = ("ID", "Название", "Применение", "Кол-во", "Цена", "Страна")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120)
tree.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

show_all()

root.mainloop()
conn.close()