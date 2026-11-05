import tkinter as tk


def on_greet():
    name = entry.get().strip()
    if name:
        label.config(text=f"Привет, {name}!")
    else:
        label.config(text="Привет, гость!")


root = tk.Tk()
root.title("Мой калькулятор")
root.geometry("420x320")

entry = tk.Entry(root)
entry.pack(pady=20)

button = tk.Button(root, text="Поздороваться", command=on_greet)
button.pack(pady=10)

label = tk.Label(root, text="Привет!")
label.pack(expand=True)

root.mainloop()