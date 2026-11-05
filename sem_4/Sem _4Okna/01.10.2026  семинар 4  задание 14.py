import tkinter as tk


def сложение():
    a = int(entry1.get().strip())
    b = int(entry2.get().strip())
    s = a + b
    label.config(text=f"Результат: {s}")

root = tk.Tk()
root.title("Мой калькулятор")
root.geometry("420x320")

label1 = tk.Label(root, text="Первое число")
label1.pack(side="top", padx=20, pady=10)

entry1 = tk.Entry(root)
entry1.pack(pady=(0, 10))

label2 = tk.Label(root, text="Второе число")
label2.pack(side="top", padx=20, pady=10)

entry2 = tk.Entry(root)
entry2.pack(pady=(0, 10))

button = tk.Button(root, text="Сложить", command=сложение)
button.pack(pady=10)

label = tk.Label(root, text="Результат: —")
label.pack(expand=True)

root.mainloop()