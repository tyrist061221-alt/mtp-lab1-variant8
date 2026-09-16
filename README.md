# Лабораторная работа №1 — Система контроля версий. Работа с ней

**<Фамилия Имя Отчество>, группа <номер группы>, вариант 8, лабораторная №1**

> ⚠️ ЗАМЕНИТЕ ФИО и номер группы на свои и сделайте коммит перед отправкой боту:
> ФИО, группа, вариант и номер лабораторной должны быть указаны именно в этой строке README.md.

**Дисциплина:** «Методы и технологии программирования» (часть 1)

## Цель работы
Научиться управлять версиями Python-проектов: создавать репозиторий, коммиты,
ветки, работать с GitHub, автоматизировать проверки кода.

## Задания варианта 8

| Уровень | № задания | Формулировка | Где реализовано |
|---|---|---|---|
| Средний | 8 | Создать репозиторий на GitHub и связать его с локальным | `tasks/sredn_8_github_remote.py`, раздел «Публикация» ниже |
| Средний | 10 | Склонировать чужой репозиторий и изучить историю | `tasks/sredn_10_clone_history.py` |
| Средний | 4 | Изменить файл, сделать второй коммит | `tasks/sredn_4_second_commit.py`, история коммитов `main` |
| Повышенный | 1 | Разрешить конфликт при слиянии веток | `tasks/povysh_1_merge_conflict.py`, ветки `feature/*` |
| Повышенный | 8 | Использовать git submodules | подмодуль `libs/libmath`, `tasks/povysh_8_submodules.py` |

## Структура проекта

```
mtp-lab1-variant8/
├── .github/workflows/ci.yml     # GitHub Actions: flake8 + unittest
├── .githooks/pre-commit         # Git hook: проверка кода flake8
├── .gitignore                   # __pycache__/, *.pyc, .env и др.
├── main.py                      # основной модуль (калькулятор)
├── requirements.txt
├── tests/test_main.py           # модульные тесты (unittest)
├── tasks/                       # демонстрации заданий варианта 8
│   ├── _common.py
│   ├── sredn_4_second_commit.py
│   ├── sredn_8_github_remote.py
│   ├── sredn_10_clone_history.py
│   ├── povysh_1_merge_conflict.py
│   └── povysh_8_submodules.py
├── scripts/run_all_demos.sh     # запуск всех демонстраций
├── docs/SETUP.md                # пошаговая инструкция
└── libs/libmath                 # git submodule (отдельный репозиторий)
```

## Запуск

```bash
# 1. Основной модуль
python main.py

# 2. Тесты
python -m unittest discover -s tests -v

# 3. Демонстрации всех заданий варианта 8
bash scripts/run_all_demos.sh

# 4. Проверка стиля кода
pip install flake8
flake8 . --max-line-length=100 --exclude=.git,__pycache__,libs
```

## Ветки (Git flow)

| Ветка | Назначение |
|---|---|
| `main` | стабильный релиз |
| `develop` | интеграционная ветка |
| `feature/*` | разработка отдельных заданий (в т.ч. конфликт слияния — Повыш.1) |

## Теги (релизы)
* `v1.0.0` — первый релиз проекта.

## Соглашения о коммитах (Semantic commits)
`feat:` — новая функциональность, `fix:` — исправление, `docs:` — документация, `merge:` — слияние, `test:` — тесты, `ci:` — конфигурация CI.

## Публикация на GitHub (Средн.8, Средн.9)

```bash
git remote add origin https://github.com/USERNAME/mtp-lab1-variant8.git
git push -u origin main
git push --all && git push --tags
```

Подмодуль `libs/libmath` публикуется отдельным репозиторием
`https://github.com/USERNAME/mtp-lab1-libmath.git`.

## Автоматизация (GitHub Actions)
Workflow `.github/workflows/ci.yml` запускается на `push` в `main`/`develop`/`feature/**`
и на `pull_request` в `main`/`develop`: устанавливает flake8, проверяет стиль, запускает тесты.
