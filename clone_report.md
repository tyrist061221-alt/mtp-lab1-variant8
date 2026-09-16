\# Отчёт по заданию Средн.10 — клонирование чужого репозитория и изучение истории



\## Клонированный репозиторий



\- URL: https://github.com/psf/requests

\- Команда клонирования: `git clone --depth 200 https://github.com/psf/requests.git chuzhoy-requests`

\- Хеш HEAD на момент изучения: `dae7ef63b4df6eded86637f251fc4e3a06c3b479`



\## Последний коммит



commit dae7ef63b4df6eded86637f251fc4e3a06c3b479

Author: dependabot\[bot]

Date: Wed Sep 2 12:15:52 2026 -0600



Bump https://github.com/astral-sh/ruff-pre-commit (#7616)



\## git log --oneline (последние 30 коммитов)

dae7ef6 (HEAD -> main, origin/main, origin/HEAD) Bump https://github.com/astral-sh/ruff-pre-commit (#7616)

5460f46 Update lock-issues.yml to latest dependencies (#7609)

6af0b94 Bump https://github.com/astral-sh/ruff-pre-commit (#7608)

8f8b212 Bump https://github.com/astral-sh/ruff-pre-commit (#7606)

8068356 Bump https://github.com/astral-sh/ruff-pre-commit (#7603)

1f6589e Bump https://github.com/astral-sh/ruff-pre-commit (#7598)

414f051 Bump the actions group with 2 updates (#7596)

ded3287 Bump https://github.com/astral-sh/ruff-pre-commit (#7597)

69f8484 Bump the actions group with 3 updates (#7591)

b17c61b Bump https://github.com/astral-sh/ruff-pre-commit (#7590)

f361ead Bump https://github.com/astral-sh/ruff-pre-commit (#7562)

d38495c Fix link to AI Policy in CONTRIBUTING.md (#7576)

4c800e9 Bump actions/setup-python from 6.2.0 to 6.3.0 in the actions group (#7561)

23953c0 Bump https://github.com/astral-sh/ruff-pre-commit (#7551)

4ed3d1b Bump actions/checkout from 6.0.2 to 7.0.0 in the actions group (#7540)

d44b67e Bump https://github.com/astral-sh/ruff-pre-commit (#7536)

74c56d5 Inline pre-commit linting (#7539)

d64b9ad Bump https://github.com/astral-sh/ruff-pre-commit (#7515)

6f66281 Add hasattr checks for remaining protocol isinstance checks (#7505)

6f205ff Fix \_encode\_files detection for \_\_getattr\_\_-based file wrappers (#7502)

661970d Disable commonly ignored Pyright linting rules (#7497)

fbd0eb3 Bump https://github.com/astral-sh/ruff-pre-commit (#7503)

1190afd Add type annotation for Request.hooks (#7498)

e50e594 Improve static typing of 3rd party imports (#7496)

3be097d Bump https://github.com/astral-sh/ruff-pre-commit (#7493)

a634611 Bump github/codeql-action from 4.35.1 to 4.36.0 in the actions group (#7492)

c4367f2 Add AI Policy

cd90742 docs: indent continuation line in Session.get :param params: (#7460)

6e83187 (tag: v2.34.2) v2.34.2

84d10f0 Move Request.headers back to Mapping (#7441)

\## git shortlog -sn (вклад авторов)



162 Nate Prewitt

64 dependabot\[bot]

53 Ian Stapleton Cordasco

11 Thomas Grainger

7 Elliot Ford

7 anupam-arista

5 Mike Fiedler

3 Ata Tuzuner

3 Joren Hammudoglu

3 Kevin Kirsche

3 mayank

2 Boris Verkhovskiy

2 Bruce Adams

2 Colin Watson

2 Dimitri Papadopoulos Orfanos

2 Quentin Pradet

2 Robin

2 Seth Michael Larson

2 flysee

1 13steinj

1 AHMAD FAIZ

1 Abhishek Jha

1 Alan Yee

1 Alexandre Erwin Ittner

1 Amin Vakil

1 Arthur Woimbée

1 Ashish Kurmi

1 Branch Vincent

1 Bruno Alla

1 Calle Svensson



\## Краткий анализ истории



\*\*Активность.\*\* Репозиторий активно развивается: последние 30 коммитов покрывают

короткий промежуток времени, среди них регулярные обновления зависимостей,

правки документации, добавление типовых аннотаций и исправления багов.



\*\*Авторы.\*\* В `shortlog` видно, что основную работу ведут мейнтейнеры проекта —

Nate Prewitt (162 коммита), Ian Stapleton Cordasco (53). Значительная часть

изменений (64) — от `dependabot\[bot]`, автоматизированного бота GitHub для

обновления зависимостей. Также есть множество внешних контрибьюторов, каждый

из которых сделал 1–2 коммита, — типичная картина для популярного open-source

проекта, принимающего pull request'ы от сообщества.



\*\*Стиль коммитов.\*\* Сообщения короткие, в императиве, часто содержат номер

issue/PR в скобках: `Add AI Policy`, `Fix link to AI Policy in CONTRIBUTING.md (#7576)`,

`Bump actions/checkout from 6.0.2 to 7.0.0 in the actions group (#7540)`.

Это соответствует рекомендациям по оформлению сообщений коммитов в крупных

open-source проектах.



\*\*Ветвление и релизы.\*\* В истории видны теги (например, `v2.34.2`), то есть

проект использует семантическое версионирование. Основная работа ведётся

в ветке `main`.



\*\*Вывод.\*\* Изучение истории чужого репозитория показало, как в крупном

open-source проекте организованы процесс контрибьюции, автоматизация обновления

зависимостей и правила оформления коммитов. Полученный опыт применим и к

учебным проектам: короткие атомарные коммиты, осмысленные сообщения,

использование тегов для релизов.

