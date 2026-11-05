# Считываем входные данные
order_price = int(input())
distance = int(input())
weight = int(input())
is_urgent = int(input())

# Вычисляем базовую стоимость
if order_price >= 5000:
    base_cost = 0
elif distance <= 5:
    base_cost = 200
elif distance <= 20:
    base_cost = 400
else:
    base_cost = 700

# Вычисляем доплаты
extra_cost = 0
if weight > 20:
    extra_cost += 500
if is_urgent == 1:
    extra_cost += 300

# Считаем итоговую стоимость
total_cost = base_cost + extra_cost

# Выводим результат в нужном формате
print(f"Базовая стоимость: {base_cost}")
print(f"Доплата: {extra_cost}")
print(f"Итого: {total_cost}")
