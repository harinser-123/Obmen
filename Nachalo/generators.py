# Считываем мощности трех генераторов
p1 = int(input())
p2 = int(input())-
p3 = int(input())

# Помещаем их в список для удобства работы
powers = [p1, p2, p3]

# Находим максимальную мощность
max_power = max(powers)

# Считаем, сколько генераторов выдают такую мощность
leaders_count = powers.count(max_power)
Выводим результат в требуемом формате
print(f"Максимальная мощность: {max_power}")
print(f"Количество лидеров: {leaders_count}")