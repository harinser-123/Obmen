import tkinter as tk
from tkinter import messagebox

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Графический редактор")
        self.pen_width = 3
        self.last_x, self.last_y = None, None
        self.color = "black"

        # Меню
        menubar = tk.Menu(root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Файл")
        menubar.add_cascade(label="Файл", menu=file_menu)
        root.config(menu=menubar)

        # Холст
        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.reset_position)

        # Панель инструментов
        toolbar = tk.Frame(root)
        toolbar.pack(fill=tk.X, padx=5, pady=5)

        # Палитра цветов
        colors = ["red", "green", "blue", "black"]
        for c in colors:
            btn = tk.Button(toolbar, bg=c, width=5, command=lambda col=c: self.set_color(col))
            btn.pack(side=tk.LEFT, padx=2)

        # Поле и кнопка толщины
        tk.Label(toolbar, text="Толщина линии:").pack(side=tk.LEFT, padx=(20, 5))
        self.width_entry = tk.Entry(toolbar, width=5)
        self.width_entry.insert(0, str(self.pen_width))
        self.width_entry.pack(side=tk.LEFT, padx=2)
        tk.Button(toolbar, text="Установить толщину", command=self.set_pen_width).pack(side=tk.LEFT, padx=5)

    def set_color(self, color):
        self.color = color

    def set_pen_width(self):
        val = self.width_entry.get().strip()
        try:
            w = int(val)
            if w <= 0:
                raise ValueError
            self.pen_width = w
        except ValueError:
            messagebox.showerror("Ошибка", "Введите целое положительное число")

    def draw(self, event):
        if self.last_x and self.last_y:
            self.canvas.create_line(
                self.last_x, self.last_y, event.x, event.y,
                width=self.pen_width, fill=self.color,
                capstyle=tk.ROUND, smooth=True, splinesteps=36
            )
        self.last_x, self.last_y = event.x, event.y

    def reset_position(self, event):
        self.last_x, self.last_y = None, None

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
