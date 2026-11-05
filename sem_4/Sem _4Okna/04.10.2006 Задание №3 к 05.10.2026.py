import tkinter as tk


def сложение():
    a = int(entry1.get().strip())
    b = int(entry2.get().strip())
    с = int(entry3.get().strip())
    label.config(text=f"Результат: {a + b + с}")


def умножение():
    a = int(entry1.get().strip())
    b = int(entry2.get().strip())
    с = int(entry3.get().strip())
    label.config(text=f"Результат: {a * b * с}")


root = tk.Tk()
root.title("Калькулятор")
root.geometry("420x320")

label1 = tk.Label(root, text="Введите три числа и нажмите на кнопку для вычисления суммы")
label1.pack(pady=20)

entry1 = tk.Entry(root)
entry1.pack(pady=0)

entry2 = tk.Entry(root)
entry2.pack(pady=0)

entry3 = tk.Entry(root)
entry3.pack(pady=0)

btn_add = tk.Button(root, text="Сложить три числа", command=сложение)
btn_add.pack(pady=0)

btn_sub = tk.Button(root, text="Умножить три числа", command=умножение)
btn_sub.pack(pady=0)

label = tk.Label(root, text=" ")
label.pack(pady=1)

root.mainloop()