# Задание 2. Разработать программу с применением пакета tk, взяв в качестве условия одну любую задачу из ПЗ №№ 1 – 9.
#Задание из ПЗ 7

import tkinter as tk
from tkinter import ttk, messagebox

def get_extension():
    filepath = entry.get().strip()
    
    if not filepath:
        messagebox.showwarning("Ошибка", "Введите путь к файлу!")
        return
    
    if '.' in filepath:
        extension = filepath.split('.')[-1]
    else:
        extension = "Нет расширения"
    
    result_label.config(text=f"Расширение файла: {extension}")

# Создание окна
root = tk.Tk()
root.title("Определение расширения файла")
root.geometry("600x300")
root.resizable(False, False)

# Заголовок
title = tk.Label(root, text="Извлечение расширения файла", 
                 font=("Arial", 16, "bold"))
title.pack(pady=20)

# Поле ввода
tk.Label(root, text="Введите полное имя файла:", 
         font=("Arial", 11)).pack(anchor="w", padx=50)
entry = tk.Entry(root, width=60, font=("Arial", 11))
entry.pack(pady=10, padx=50)

# Кнопка
btn = tk.Button(root, text="Определить расширение", 
                font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",
                command=get_extension)
btn.pack(pady=15)

# Результат
result_label = tk.Label(root, text="Расширение файла: ", 
                        font=("Arial", 12), fg="blue")
result_label.pack(pady=20)

root.mainloop()