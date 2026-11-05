c = int(input())
if c < -20:
    print(f"Режим: ЭКСТРЕМАЛЬНЫЙ ХОЛОД")
elif c < 0:
    print(f"Режим: ХОЛОДНО")
elif c < 20:
    print(f"Режим: ПРОХЛАДНО")
elif c < 30:
    print(f"Режим: КОМФОРТНО")
else:
    print(f"Режим: ЖАРКО")