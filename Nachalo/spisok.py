""""List"""
"""Список - упорядоченный набор объектов"""

"""    0    1   2   3   4   """
num = [22, 33, 44, 55, 99]
"""    -5  -4  -3  -2  -1  """
print(num[0])
print(num[2])
print(num[1:-2])
print(num[::2])
print(num[2:])
print(num[2::-1])
print(num[::-1])

#nn = num
#nn = num[:]
# nn = num.copy()
# num[1] = 3333
print(num, id(num))
print(nn, id(nn))
print(nn is num)



tp = (22, 33, 44, 99)
## K = 7,                  # запятая
## print(K, type(K), K[0])
k, *i, z = 7, 5, 9, 10, 1, 32, 56, 100,                  # запятая
print(k, i, z)  # 7 [5, 9, 10, 1, 32, 56] 100
print(k, *i, z)  # распаковка
tp = ("login", "password")
print(tp, id(tp))
buf = list(tp)
buf[-1] = "new_password"
#print(buf)
tp = tuple(buf)
print(tp, id(tp))
# тернарный оператор