import math


def square(side):
    return math.ceil(side * side)


length_side = int(input("Введите длину стороны: "))
print(f"Площадь квадрата равна {square(length_side)}")
