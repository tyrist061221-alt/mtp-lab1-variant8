"""Средн.10 — склонировать чужой репозиторий и изучить историю."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import init_repo, sh, write  # noqa: E402

APP = '"""Учебное приложение (шаг {n})."""\n\nSTEP = {n}\n'


def main():
    """Создание «чужого» репозитория, его клонирование и анализ истории."""
    with tempfile.TemporaryDirectory() as base:
        src = os.path.join(base, "someone_else_repo")
        os.makedirs(src)
        init_repo(src)
        for i in range(1, 6):
            write(os.path.join(src, "app.py"), APP.format(n=i))
            sh("git add app.py", src)
            sh(f'git commit -m "feat: step {i}"', src)

        sh("git clone someone_else_repo cloned_repo", base)
        dst = os.path.join(base, "cloned_repo")

        sh("git remote -v", dst)
        sh("git log --oneline --graph --decorate", dst)
        sh("git shortlog -sn HEAD", dst)
        sh("git log --stat -1", dst)

        count = len(sh("git log --oneline", dst).stdout.splitlines())
        assert count == 5, f"Ожидалось 5 коммитов, получено {count}"
        assert os.path.exists(os.path.join(dst, "app.py"))
        print(f"РЕЗУЛЬТАТ: Средн.10 выполнено — репозиторий клонирован, "
              f"в истории {count} коммитов.")


if __name__ == "__main__":
    main()
