s = input()
try:
    n = int(s)
except ValueError:
    print("Это не число")
else:
    if n < 1 or n > 120:
        print("Нужно от 1 до 120 минут")
    else:
        print(f"Таймер: {n} мин")
