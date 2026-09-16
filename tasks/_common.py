"""Общие утилиты для демонстраций задач лабораторной работы №1 (вариант 8)."""
import subprocess


def sh(cmd, cwd, check=True):
    """Выполнить shell-команду в каталоге cwd, напечатать вывод и вернуть результат."""
    res = subprocess.run(
        cmd, shell=True, cwd=cwd, capture_output=True,
        text=True, stdin=subprocess.DEVNULL,
    )
    print(f"$ {cmd}")
    out = (res.stdout + res.stderr).strip()
    if out:
        print(out)
    if check and res.returncode != 0:
        raise RuntimeError(f"Команда завершилась с ошибкой ({res.returncode}): {cmd}")
    return res


def write(path, text):
    """Записать текст в файл в кодировке UTF-8."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def read(path):
    """Прочитать текст из файла в кодировке UTF-8."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def init_repo(path):
    """Инициализировать репозиторий с главной веткой main и локальными настройками."""
    sh("git init -b main", path)
    sh('git config user.name "Student"', path)
    sh('git config user.email "student@example.com"', path)
