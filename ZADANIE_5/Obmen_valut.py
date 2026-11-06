from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk

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


root = Tk()
root.title('Курсы обмена валют')
root.geometry('460x440')

# --- Базовая валюта 1 ---
Label(root, text='Базовая валюта').pack(pady=(15, 5))
base1_combobox = ttk.Combobox(root, values=list(currencies.keys()), justify='center')
base1_combobox.pack(pady=0)
base1_combobox.current(0) # По умолчанию EUR
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


root.mainloop()