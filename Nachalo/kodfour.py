n = int(input())
thousands = n // 1000
thousandsost = n % 1000
hundreds = thousandsost // 100
hundredsost = thousandsost % 100
tens = hundredsost // 10
tensost = hundredsost % 10
ones = tensost % 10


print(f"Тысячи: {thousands}")
print(f"Сотни: {hundreds}")
print(f"Десятки: {tens}")
print(f"Единицы: {ones}")
print(f"Сумма цифр: {thousands + hundreds + tens + ones}")
print(f"Произведение цифр: {thousands * hundreds * tens * ones}")
print(f"Обратный код: {ones}{tens}{hundreds}{thousands}")