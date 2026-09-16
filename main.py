"""Учебный Python-проект для лабораторной работы №1 (вариант 8).

Дисциплина: «Методы и технологии программирования» (часть 1).
Второй коммит: добавлены функции power и factorial (задание Средн.4).
"""

VERSION = "1.1.0"


def add(a, b):
    """Сложение двух чисел."""
    return a + b


def subtract(a, b):
    """Вычитание двух чисел."""
    return a - b


def multiply(a, b):
    """Умножение двух чисел."""
    return a * b


def divide(a, b):
    """Деление с проверкой деления на ноль."""
    if b == 0:
        raise ValueError("Деление на ноль недопустимо")
    return a / b


def power(base, exp):
    """Возведение в степень."""
    return base ** exp


def factorial(n):
    """Факториал числа n."""
    if n < 0:
        raise ValueError("n должно быть неотрицательным")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def main():
    """Точка входа."""
    print(f"mtp-calc v{VERSION}")
    print("2 + 3 =", add(2, 3))
    print("2 ** 10 =", power(2, 10))
    print("5! =", factorial(5))


if __name__ == "__main__":
    main()
