import tkinter as tk


def on_start():
    label.config(text="Готов к расчётам!")


root = tk.Tk()
root.title("Мой калькулятор")
root.geometry("420x320")

label = tk.Label(root, text="Привет!")
label.pack(expand=True)

button = tk.Button(root, text="Начать", command=on_start)
button.pack(pady=20)

root.mainloop()
