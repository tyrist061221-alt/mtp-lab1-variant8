"""Учебный Python-проект для лабораторной работы №1 (вариант 8).

Дисциплина: «Методы и технологии программирования» (часть 1).
Первый коммит: базовые арифметические функции.
"""

VERSION = "1.0.0"


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


def main():
    """Точка входа."""
    print(f"mtp-calc v{VERSION}")
    print("2 + 3 =", add(2, 3))
    print("10 - 4 =", subtract(10, 4))
    print("3 * 4 =", multiply(3, 4))
    print("9 / 3 =", divide(9, 3))


if __name__ == "__main__":
    main()
