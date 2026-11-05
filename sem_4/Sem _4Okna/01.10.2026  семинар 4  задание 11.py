import tkinter as tk

count = 0

def on_check():
    global count
    count += 1
    label.config(text=f"Нажатий: {count}")

root = tk.Tk()
root.title("Мой калькулятор")
root.geometry("420x320")

label = tk.Label(root, text="Нажатий: 0")
label.pack(expand=True)

button = tk.Button(root, text="Проверить", command=on_check)
button.pack(pady=20)

root.mainloop()