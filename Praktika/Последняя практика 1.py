Сумма = int(input())

if Сумма < 1000:
    print("Доставка: 199 рублей")
elif 1000 <= Сумма <= 4999:
    print("Доставка: 99 рублей")
else:  # amount >= 5000
    print("Доставка: бесплатно")

# в цикле

# while True:
#     line = input()
#     if line == "":          # выход при пустой строке
#         break
#     amount = int(line)
#
#     if amount <= 999:
#         print("Доставка: 199 рублей")
#     elif 1000 <= amount <= 4999:
#         print("Доставка: 99 рублей")
#     else:  # amount >= 5000
#         print("Доставка: бесплатно")