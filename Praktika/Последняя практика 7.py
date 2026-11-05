from tkinter import *


def start():
    # Получаем текст из поля ввода
    text = entry.get()

    try:
        minutes = int(text)
    except ValueError:
        # Если в поле не число
        result.config(text="Это не число")
        return

    # Проверка диапазона: от 1 до 120 включительно
    if minutes < 1 or minutes > 120:
        result.config(text="Нужно от 1 до 120 минут")
    else:
        # Корректное значение
        result.config(text=f"Таймер: {minutes} мин")


# Создаём главное окно
root = Tk()
root.title("Таймер корма")
root.geometry("360x200")

# Надпись-подсказка
label_prompt = Label(root, text="Сколько минут варить?")
label_prompt.pack(pady=10)

# Поле ввода
entry = Entry(root)
entry.pack(pady=5)

# Кнопка
btn = Button(root, text="Запустить", command=start)
btn.pack(pady=10)

# Метка результата (изначально «Таймер не запущен»)
result = Label(root, text="Таймер не запущен")
result.pack(pady=5)

# Запуск цикла обработки событий
root.mainloop()