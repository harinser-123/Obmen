import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Графический редактор")

control_panel = tk.Frame(root)
control_panel.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

tk.Label(control_panel, text="Толщина пера:").pack(side=tk.LEFT, padx=5)

entry_thickness = tk.Entry(control_panel, width=10)
entry_thickness.insert(0, "2")
entry_thickness.pack(side=tk.LEFT, padx=5)

current_thickness = 2
x_last, y_last = 0, 0


def update_thickness():
    global current_thickness
    user_input = entry_thickness.get()

    try:
        new_thickness = int(user_input)
        if new_thickness > 0:
            current_thickness = new_thickness
            print(f"Толщина изменена на: {current_thickness}")
        else:
            messagebox.showwarning("Ошибка", "Толщина должна быть положительным числом!")

    except ValueError:
        messagebox.showerror("Ошибка", f"'{user_input}' - это не целое число. Введите число, например: 5")


def start_draw(event):
    global x_last, y_last
    x_last = event.x
    y_last = event.y


def draw(event):
    global x_last, y_last
    canvas.create_line(x_last, y_last, event.x, event.y,
                       fill="black",
                       width=current_thickness,
                       capstyle=tk.ROUND)

    x_last = event.x
    y_last = event.y


canvas = tk.Canvas(root, bg="white", width=600, height=400)
canvas.pack(fill=tk.BOTH, expand=True)

canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)

button_set = tk.Button(control_panel, text="Применить", command=update_thickness)
button_set.pack(side=tk.LEFT, padx=5)

root.mainloop()