# Считываем текущее время и время будильника
now_str = input()
alarm_str = input()

# Переводим время в минуты от полуночи
# Срезы: [0:2] — часы, [3:5] — минуты
now_h = int(now_str[0:2])
now_m = int(now_str[3:5])
alarm_h = int(alarm_str[0:2])
alarm_m = int(alarm_str[3:5])

now_total = now_h * 60 + now_m
alarm_total = alarm_h * 60 + alarm_m

# Вычисляем разницу в минутах.
# Если alarm_total <= now_total, разница будет отрицательной или нулём.
# % 1440 «заворачивает» её на следующие сутки: например, -965 станет 475.
diff_minutes = (alarm_total - now_total) % 1440

# Переводим минуты обратно в часы и минуты
hours = diff_minutes // 60
minutes = diff_minutes % 60

print(f"Через {hours} ч {minutes} мин")