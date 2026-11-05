name_raw = input()
name = name_raw.strip()

if name == "":
    print("Ошибка: пустое имя")
elif len(name) > 12:
    print("Ошибка: слишком длинное имя")
elif any(ch.isdigit() for ch in name):
    print("Ошибка: в имени цифры")
else:
    print(f"Имя принято: {name}")