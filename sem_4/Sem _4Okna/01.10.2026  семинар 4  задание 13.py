import tkinter as tk


def on_double():
    n = int(entry.get().strip())
    r = 2 * n
    label.config(text=f"Результат: {r}")


root = tk.Tk()
root.title("Мой калькулятор")
root.geometry("420x320")

entry = tk.Entry(root)
entry.pack(pady=20)

button = tk.Button(root, text="Удвоить", command=on_double)
button.pack(pady=10)

label = tk.Label(root, text="Результат: —")
label.pack(expand=True)

root.mainloop()