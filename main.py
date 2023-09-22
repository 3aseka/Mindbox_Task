import math

# Выбор фигуры
def start():
    while True:
        try:
            name = int(input('Введите номер фигуры:\n'
                            '1 - Круг\n'
                            '2 - Треугольник\n'))
        except Exception:
            print('Не корректные данные!\n')
        else:
            return figur(name)

# Вводим данные о фигуре
def figur(name):
    if name == 1:
        r = float(input('Введите радиус, чтобы найти площадь круга.\n'))
        return circle(r)

    elif name == 2:
        while True:
            try:
                a, b, c = map(float, input('Введите размер сторон треугольника через пробел.\n').split())
            except Exception:
                print('Ошибка, данные введены не верно\n')
            else:
                return triangle(a, b, c)

    else:
        print('Неверное число\n')
        return start()

# Нахожение круга
def circle(r):
    circ = (r**2) * math.pi
    print(f"Площадь круга == {round(circ, 2)}\n")

    return start()

# Нахождение треугольника
def triangle(a, b, c):

    if not(a + b > c and a + c > b and b + c > a):
        print('Такого треугольника нет\n')
    else:
        p = (a + b + c) / 2
        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        print(f"Площадь треугольника == {round(s, 2)}\n")

    return start()

if __name__ == '__main__':
    start()


