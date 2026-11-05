from tkinter import *
from tkinter import messagebox

def is_time(s):
    # Проверка длины строки
    if len(s) != 5:
        return False
    # Проверка двоеточия на позиции 2
    if s[2] != ':':
        return False
    # Проверка, что остальные символы — цифры
    digits = "0123456789"
    if s[0] not in digits or s[1] not in digits or s[3] not in digits or s[4] not in digits:
        return False

    # Преобразуем в числа и проверяем диапазоны
    hours = int(s[0:2])
    minutes = int(s[3:5])

    if hours < 0 or hours > 23:
        return False
    if minutes < 0 or minutes > 59:
        return False

    return True


def to_minutes(s):
    # Функция гарантированно вызывается только для корректного времени (по логике set_alarm)
    hours = int(s[0:2])
    minutes = int(s[3:5])
    return hours * 60 + minutes


def set_alarm():
    now_str = now_entry.get()
    alarm_str = alarm_entry.get()

    # Проверяем оба поля
    if not is_time(now_str) or not is_time(alarm_str):
        messagebox.showerror("Ошибка", "Время нужно в формате ЧЧ:ММ")
        result.config(text="Напоминание не поставлено")
        return

    # Переводим в минуты от полуночи
    now_total = to_minutes(now_str)
    alarm_total = to_minutes(alarm_str)

    # Вычисляем разницу с учётом перехода на следующие сутки
    diff_minutes = (alarm_total - now_total) % 1440

    # Конвертируем обратно в часы и минуты
    hours = diff_minutes // 60
    minutes = diff_minutes % 60

    result.config(text=f"Сработает через {hours} ч {minutes} мин")


window = Tk()
window.title("Напоминалка")
window.geometry("380x240")

Label(text="Сейчас:").pack()
now_entry = Entry()
now_entry.pack()

Label(text="Напомнить в:").pack()
alarm_entry = Entry()
alarm_entry.pack()

Button(text="Поставить", command=set_alarm).pack(pady=10)

result = Label(text="Напоминание не поставлено")
result.pack()

window.mainloop()