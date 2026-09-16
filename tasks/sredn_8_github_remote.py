"""Средн.8 — создать репозиторий на GitHub и связать его с локальным."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import init_repo, sh, write  # noqa: E402

REMOTE = "https://github.com/USERNAME/mtp-lab1-variant8.git"

MAIN_PY = '''"""Учебный Python-проект для лабораторной работы №1."""

VERSION = "1.0.0"


def main():
    """Точка входа."""
    print(f"mtp-lab1 v{VERSION}")


if __name__ == "__main__":
    main()
'''


def main():
    """Связывание локального репозитория с удалённым на GitHub."""
    with tempfile.TemporaryDirectory() as d:
        init_repo(d)
        write(os.path.join(d, "main.py"), MAIN_PY)
        sh("git add main.py", d)
        sh('git commit -m "feat: initial project structure"', d)

        sh(f"git remote add origin {REMOTE}", d)
        remotes = sh("git remote -v", d).stdout

        res = sh("git push -u origin main", d, check=False)
        if res.returncode != 0:
            print("ПРИМЕЧАНИЕ: в песочнице push к GitHub недоступен (нет сети/прав).")
            print("На вашей машине после создания репозитория команда отправит код.")
        else:
            print("Push на GitHub выполнен успешно.")

        assert "origin" in remotes and REMOTE in remotes, "origin не настроен"
        print("РЕЗУЛЬТАТ: Средн.8 выполнено — origin связан с GitHub-репозиторием.")


if __name__ == "__main__":
    main()
