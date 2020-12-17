# !/usr/bin/evn python3
# -*- config: utf-8 -*-

import math

# Решите следующую задачу: в основной ветке программы вызывается функция cylinder(),
# которая вычисляет площадь цилиндра. В теле cylinder() определена функция circle(),
# вычисляющая площадь круга по формуле pi*(r^2). В теле cylinder() у пользователя
# спрашивается, хочет ли он получить только площадь боковой поверхности цилиндра,
# которая вычисляется по формуле 2*pi*r*h, или полную площадь цилиндра. В последнем
# случае к площади боковой поверхности цилиндра должен добавляться удвоенный результат
# вычислений функции circle().


def circle(r):
    return math.pi * (r ** 2)


def cylinder(h, r, full=True):
    side = 2 * math.pi * r * h
    if full:
        return side + 2 * circle(r)
    else:
        return side


if __name__ == '__main__':
    y = int(input('Enter radius: '))
    x = int(input('Enter height: '))
    c = input("side or full?")
    s = cylinder(x, y, full=(c == 'full'))
    print(s)
