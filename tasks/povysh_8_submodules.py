"""Повыш.8 — использовать git submodules."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import init_repo, sh, write  # noqa: E402

LIB = '''"""Небольшая библиотека, подключаемая как git submodule."""


def add(a, b):
    """Сложение двух чисел."""
    return a + b


def is_even(n):
    """Проверка чётности числа."""
    return n % 2 == 0
'''

LIB_README = "# libmath\n\nУчебная библиотека для демонстрации git submodules.\n"

APP = '''"""Приложение, использующее код из подмодуля libs/libmath."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "libs", "libmath"))

from libmath import add, is_even  # noqa: E402


def main():
    """Точка входа."""
    print("2 + 3 =", add(2, 3))
    print("4 чётное?", is_even(4))


if __name__ == "__main__":
    main()
'''


def main():
    """Подключение отдельного репозитория как git submodule и проверка работы."""
    with tempfile.TemporaryDirectory() as base:
        lib = os.path.join(base, "libmath")
        app = os.path.join(base, "app")
        os.makedirs(lib)
        os.makedirs(app)

        init_repo(lib)
        write(os.path.join(lib, "libmath.py"), LIB)
        sh("git add libmath.py", lib)
        sh('git commit -m "feat: add libmath library"', lib)
        write(os.path.join(lib, "README.md"), LIB_README)
        sh("git add README.md", lib)
        sh('git commit -m "docs: add README for libmath"', lib)

        init_repo(app)
        write(os.path.join(app, "main.py"), APP)
        sh("git add main.py", app)
        sh('git commit -m "feat: add main application"', app)

        sh(f'git -c protocol.file.allow=always submodule add "{lib}" libs/libmath', app)
        sh('git commit -m "feat: add libmath as git submodule"', app)

        sh("git submodule status", app)
        sh("git submodule foreach 'git log --oneline -1'", app)
        sh("git ls-files --stage | grep 160000", app)

        assert os.path.exists(os.path.join(app, ".gitmodules")), ".gitmodules не создан"
        assert os.path.exists(os.path.join(app, "libs", "libmath", "libmath.py"))
        sh("python3 main.py", app)
        print("РЕЗУЛЬТАТ: Повыш.8 выполнено — подмодуль подключён и его код исполняется.")


if __name__ == "__main__":
    main()
