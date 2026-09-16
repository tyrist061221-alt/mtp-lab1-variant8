"""Средн.4 — изменить файл, сделать второй коммит."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import init_repo, sh, write  # noqa: E402

V1 = '''"""Учебный модуль калькулятора (версия 1)."""

VERSION = "1.0.0"


def add(a, b):
    """Сложение."""
    return a + b


def subtract(a, b):
    """Вычитание."""
    return a - b


def main():
    """Точка входа."""
    print(f"calc v{VERSION}: 2 + 3 = {add(2, 3)}")


if __name__ == "__main__":
    main()
'''

V2 = '''"""Учебный модуль калькулятора (версия 2).

Второй коммит: добавлены функции power и factorial.
"""

VERSION = "1.1.0"


def add(a, b):
    """Сложение."""
    return a + b


def subtract(a, b):
    """Вычитание."""
    return a - b


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
    print(f"calc v{VERSION}: 2 + 3 = {add(2, 3)}, 2 ** 10 = {power(2, 10)}")


if __name__ == "__main__":
    main()
'''


def main():
    """Демонстрация двух коммитов: второй содержит изменённый файл."""
    with tempfile.TemporaryDirectory() as d:
        init_repo(d)

        write(os.path.join(d, "main.py"), V1)
        sh("git add main.py", d)
        sh('git commit -m "feat: add calculator module (version 1)"', d)
        first = sh("git log -1 --format=%H", d).stdout.strip()

        write(os.path.join(d, "main.py"), V2)
        sh("git add main.py", d)
        sh('git commit -m "feat: add power and factorial functions"', d)
        second = sh("git log -1 --format=%H", d).stdout.strip()

        log = sh("git log --oneline", d).stdout
        count = len([line for line in log.splitlines() if line.strip()])

        print(f"Хеш 1-го коммита: {first}")
        print(f"Хеш 2-го коммита: {second}")
        print(f"Всего коммитов: {count}")
        assert count == 2, "Ожидалось ровно два коммита"
        assert first != second
        sh("python3 main.py", d)
        print("РЕЗУЛЬТАТ: Средн.4 выполнено — файл изменён, создан второй коммит.")


if __name__ == "__main__":
    main()
