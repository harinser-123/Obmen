from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests

currencies = {
    'EUR': 'Евро',
    'USD': 'Американский доллар',
    'JPY': 'Японская йена',
    'GBP': 'Фунт стерлингов',
    'AUD': 'Австралийский доллар',
    'CAD': 'Канадский доллар',
    'CHF': 'Швейцарский франк',
    'CNY': 'Китайский юань',
    'RUB': 'Российский рубль',
    'KZT': 'Казахстанский тенге',
    'UZS': 'Узбекский сум'
}

def update_label(event, combobox, label):
    code = combobox.get().strip().upper()
    if code in currencies:
        label.config(text=currencies[code])
    else:
        label.config(text='')

def exchange():
    target_code = target_combobox.get().strip().upper()
    base1_code = base1_combobox.get().strip().upper()
    base2_code = base2_combobox.get().strip().upper()

    if not target_code:
        mb.showwarning('Внимание', 'Выберите целевую валюту')
        return

    # Сброс результатов
    res1_label.config(text='')
    res2_label.config(text='')

    # Обработка первой базовой валюты
    if base1_code:
        try:
            resp = requests.get(f'https://open.er-api.com/v6/latest/{base1_code}', timeout=10)
            resp.raise_for_status()
            data = resp.json()
            if target_code in data.get('rates', {}):
                rate = data['rates'][target_code]
                res1_label.config(text=f'{currencies.get(base1_code, base1_code)} → {currencies.get(target_code, target_code)}: {rate:.4f}')
            else:
                res1_label.config(text=f'{currencies.get(base1_code, base1_code)}: валюта не найдена')
        except Exception as e:
            res1_label.config(text=f'{currencies.get(base1_code, base1_code)}: ошибка соединения')

    # Обработка второй базовой валюты
    if base2_code:
        try:
            resp = requests.get(f'https://open.er-api.com/v6/latest/{base2_code}', timeout=10)
            resp.raise_for_status()
            data = resp.json()
            if target_code in data.get('rates', {}):
                rate = data['rates'][target_code]
                res2_label.config(text=f'{currencies.get(base2_code, base2_code)} → {currencies.get(target_code, target_code)}: {rate:.4f}')
            else:
                res2_label.config(text=f'{currencies.get(base2_code, base2_code)}: валюта не найдена')
        except Exception as e:
            res2_label.config(text=f'{currencies.get(base2_code, base2_code)}: ошибка соединения')

root = Tk()
root.title('Курсы обмена валют')
root.geometry('360x340')

# --- Базовая валюта 1 ---
Label(root, text='Базовая валюта').pack(pady=(15, 5))
base1_combobox = ttk.Combobox(root, values=list(currencies.keys()), justify='center')
base1_combobox.pack(pady=0)
base1_combobox.current(0)  # По умолчанию EUR
base1_name_label = ttk.Label(root, text=currencies['EUR'], font=('Arial', 10))
base1_name_label.pack(pady=(2, 10))
base1_combobox.bind('<<ComboboxSelected>>', lambda e: update_label(e, base1_combobox, base1_name_label))

# --- Вторая базовая валюта ---
Label(root, text='Вторая базовая валюта').pack()
base2_combobox = ttk.Combobox(root, values=list(currencies.keys()), justify='center')
base2_combobox.pack(pady=0)
base2_combobox.current(1)  # По умолчанию USD
base2_name_label = ttk.Label(root, text=currencies['USD'], font=('Arial', 10))
base2_name_label.pack(pady=(2, 10))
base2_combobox.bind('<<ComboboxSelected>>', lambda e: update_label(e, base2_combobox, base2_name_label))

# --- Целевая валюта ---
Label(root, text='Целевая валюта').pack()
target_combobox = ttk.Combobox(root, values=list(currencies.keys()), justify='center')
target_combobox.pack(pady=0)
target_combobox.current(8)  # По умолчанию RUB
target_name_label = ttk.Label(root, text=currencies['RUB'], font=('Arial', 10))
target_name_label.pack(pady=(2, 15))
target_combobox.bind('<<ComboboxSelected>>', lambda e: update_label(e, target_combobox, target_name_label))

# --- Кнопка ---
btn = Button(root, text='Получить курс обмена', command=exchange, width=25)
btn.pack(pady=5)

# --- Результаты (под кнопкой, как продолжение формы) ---
res1_label = ttk.Label(root, text='', font=('Arial', 11, 'bold'), foreground='#005500')
res1_label.pack(pady=(10, 5))

res2_label = ttk.Label(root, text='', font=('Arial', 11, 'bold'), foreground='#005500')
res2_label.pack(pady=(0, 10))

root.mainloop()