s = input()
try:
  n = int(s)
  print(f"Таймер: {n} мин")
except ValueError:
  print("Это не число")
