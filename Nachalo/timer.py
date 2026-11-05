n = int(input())

days = n // 86400
daysost = n % 86400
hours = daysost // 3600
hoursost = daysost % 3600
minutes = hoursost // 60
minutesost = hoursost % 60
sec = minutesost % 60

print(f"Дни: {days}")
print(f"Часы: {hours}")
print(f"Минуты: {minutes}")
print(f"Секунды: {sec}")