n = int(input())
k = int(input())

floor = (n + k - 1) // k
position = n % k
if position == 0:
   position = k
print(f"Этаж: {floor}")
print(f"Позиция на этаже: {position}")