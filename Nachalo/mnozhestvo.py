"""Множество (set) неупорядоченный
набор уникальных объектов
(любые неизменяемые типы данных)
"""
ls = [22, 22, 22, 33, 33]
st = set(ls)
print(st)
st.clear()
st = {22, 33, 44}
print(st)

st.add(100)    #добавляет один объект, в том числе кортеж
st.update({2, 3}) #воспринимает как коллекцию
print(st)
n = st.pop()    #удаление известного
st.remove(3) # метод удаления
st.discard(2)  #тоже но ошибку не выдает
print(n)
print(st)

# print(st)
# for i in st:
#     print(i)

st1 = {3, 4, 33}
st2 = {3, 4, 44}

# res = st1.union(st2)  #объединение множеств
res = st1 | st2   # тоже самое

res = st1.intersection(st2)  # пересечение множеств
res = st1 & st2

res = st1.difference(st2)  #вычитание множеств
res = st2 - st1
print(res)

res = st1.symmetric_difference(st2)  #симметрическая разница какие элементы разные
res = st1 ^ st2
print(res)
st1 = {3, 4, 33}
st2 = {3, 4, 44}
st3 = {3, 4}
print(st3.issubset(st2))
print(st1.issuperset(st3))
