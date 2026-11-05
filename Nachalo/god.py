g = int(input())

if g % 400 == 0 or (g % 4 == 0 and g % 100 != 0):
    print("Год: ВИСОКОСНЫЙ")
else:
    print("Год: НЕВИСОКОСНЫЙ")