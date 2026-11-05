Pupils1 = int(input())
Pupils2 = int(input())
Pupils3 = int(input())
desks1 = (Pupils1 + 1) // 2
desks2 = (Pupils2 + 1) // 2
desks3 = (Pupils3 + 1) // 2
total = desks1 + desks2 + desks3

print(f"Первый класс: {desks1}")
print(f"Второй класс: {desks2}")
print(f"Третий класс: {desks3}")
print(f"Всего парт: {total}")