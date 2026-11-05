
import tkinter as tk


def on_add():
    a = int(entry1.get().strip())
    b = int(entry2.get().strip())
    label.config(text=f"Результат: {a + b}")


def on_sub():
    a = int(entry1.get().strip())
    b = int(entry2.get().strip())
    label.config(text=f"Результат: {a - b}")


root = tk.Tk()
root.title("Мой калькулятор")
root.geometry("420x320")

label1 = tk.Label(root, text="Первое число")
label1.pack(pady=(20, 0))

entry1 = tk.Entry(root)
entry1.pack(pady=(0, 10))

label2 = tk.Label(root, text="Второе число")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack(pady=(0, 10))

btn_add = tk.Button(root, text="Сложить", command=on_add)
btn_add.pack(side=tk.LEFT, padx=80, pady=10)

btn_sub = tk.Button(root, text="Вычесть", command=on_sub)
btn_sub.pack(side=tk.RIGHT, padx=80, pady=10)

label = tk.Label(root, text="Результат: —")
label.pack(expand=True)

root.mainloop()

