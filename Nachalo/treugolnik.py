a = int(input())
b = int(input())
c = int(input())

if (a + b > c) and (a + c > b) and (b + c > a):

    if a == b == c:
        print(f"Тип: РАВНОСТОРОННИЙ")
    elif a == b or b == c or a == c:
        print("Тип: РАВНОБЕДРЕННЫЙ")
    else:
        print("Тип: РАЗНОСТОРОННИЙ")

else:
    print("Тип: ТРЕУГОЛЬНИК НЕ СУЩЕСТВУЕТ")