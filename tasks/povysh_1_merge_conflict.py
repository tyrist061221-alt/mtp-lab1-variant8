"""Повыш.1 — разрешить конфликт при слиянии веток."""
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import init_repo, read, sh, write  # noqa: E402


def main():
    """Воспроизведение и разрешение конфликта слияния двух веток."""
    with tempfile.TemporaryDirectory() as d:
        init_repo(d)
        cfg = os.path.join(d, "settings.txt")

        write(cfg, "mode = base\nversion = 1\n")
        sh("git add settings.txt", d)
        sh('git commit -m "feat: add base settings"', d)

        sh("git checkout -b feature", d)
        write(cfg, "mode = feature\nversion = 1\n")
        sh("git add settings.txt", d)
        sh('git commit -m "feat: change mode in feature branch"', d)

        sh("git checkout main", d)
        write(cfg, "mode = main\nversion = 1\n")
        sh("git add settings.txt", d)
        sh('git commit -m "fix: update settings on main"', d)

        res = sh("git merge feature", d, check=False)
        merged_output = res.stdout + res.stderr
        assert res.returncode != 0, "Ожидался конфликт при слиянии"
        assert "CONFLICT" in merged_output, "Git не сообщил о конфликте"
        print("Конфликт слияния успешно воспроизведён.")

        sh("git status --short", d)
        assert "<<<<<<<" in read(cfg), "В файле нет маркеров конфликта"

        write(cfg, "mode = main+feature\nversion = 1\n")
        sh("git add settings.txt", d)
        sh('git commit -m "merge: resolve conflict in settings.txt"', d)

        sh("git log --oneline --graph --all", d)
        sh("git branch --merged main", d)

        final = read(cfg)
        assert "<<<<<<<" not in final and ">>>>>>>" not in final, "Маркеры не удалены"
        assert sh("git status --porcelain", d).stdout.strip() == ""
        print("РЕЗУЛЬТАТ: Повыш.1 выполнено — конфликт разрешён, слияние зафиксировано.")


if __name__ == "__main__":
    main()
