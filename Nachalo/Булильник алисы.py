from tkinter import *
from tkinter import messagebox
import time


def update_clock():
    """Обновляет часы на экране каждую секунду"""
    now = time.strftime('%H:%M:%S')
    screen_time.config(text=now)
    check_alarm()
    root.after(1000, update_clock)


def check_alarm():
    """Проверяет, не пора ли звенеть"""
    global alarm_triggered
    if alarm_set and not alarm_triggered:
        now = time.strftime('%H:%M')
        if now == alarm_value:
            alarm_triggered = True
            messagebox.showinfo('Будильник', '⏰ ВСТАВАЙ! Час пробуждения!')
            # Сбрасываем состояние, чтобы можно было включить снова
            disable_alarm()


def disable_alarm():
    """Выключает будильник и обновляет интерфейс"""
    global alarm_set, alarm_value, alarm_triggered
    alarm_set = False
    alarm_value = ""
    alarm_triggered = False

    # Обновляем кнопки и статус
    btn_enable.pack(side=LEFT, padx=10, pady=5)
    btn_disable.pack_forget()  # скрываем кнопку «Отключить»
    label_status.config(text='Будильник выключен', fg='gray')


def enable_alarm():
    """Включает будильник после проверки ввода"""
    global alarm_set, alarm_value, alarm_triggered

    entered = entry_time.get().strip()
    try:
        hours, minutes = entered.split(':')
        hours, minutes = int(hours), int(minutes)
        if not (0 <= hours <= 23 and 0 <= minutes <= 59):
            raise ValueError
    except ValueError:
        messagebox.showerror('Ошибка', 'Введите время в формате ЧЧ:ММ\nНапример: 07:30')
        return

    alarm_value = entered
    alarm_set = True
    alarm_triggered = False

    # Обновляем кнопки и статус
    btn_enable.pack_forget()      # скрываем «Включить»
    btn_disable.pack(side=LEFT, padx=10, pady=5)  # показываем «Отключить»
    label_status.config(text=f'Будильник на {alarm_value}', fg='lime')


# --- Окно ---
root = Tk()
root.title('Будильник')
root.config(background='black')

WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
X = 400
Y = 250
root.geometry(f"{X}x{Y}+{WIDTH // 2 - X // 2}"
             f"+{HEIGHT // 2 - Y // 2 - 25}")
root.resizable(False, False)

# --- Часы ---
screen_time = Label(root, text='00:00:00', font='Arial 50')
screen_time.config(bg='black', fg='lime')
screen_time.pack(pady=10)

# --- Поле ввода времени ---
entry_time = Entry(root, font='Arial 20', justify='center')
entry_time.insert(0, '07:30')
entry_time.pack(pady=5)

# --- Кнопки (в одном контейнере, чтобы стояли рядом) ---
btn_frame = Frame(root, bg='black')
btn_frame.pack(pady=5)

btn_enable = Button(btn_frame, text='Включить', font='Arial 16',
                    bg='lime', command=enable_alarm)
btn_enable.pack(side=LEFT, padx=10, pady=5)

btn_disable = Button(btn_frame, text='Отключить', font='Arial 16',
                     bg='red', command=disable_alarm)
# Сначала скрываем, потому что будильник выключен
btn_disable.pack_forget()

# --- Статус ---
label_status = Label(root, text='Будильник выключен', font='Arial 12',
                     bg='black', fg='gray')
label_status.pack(pady=5)

# --- Переменные состояния ---
alarm_set = False
alarm_value = ""
alarm_triggered = False

# --- Запуск ---
update_clock()
root.mainloop()