# Пошаговая инструкция по сдаче лабораторной работы №1 (вариант 8)

## Шаг 0. Подготовка архива
Распаковать полученный архив `mtp-lab1-variant8.zip`. Внутри — готовая рабочая
копия репозитория (с папкой `.git`) и отдельная папка `mtp-lab1-libmath`
(репозиторий подмодуля).

## Шаг 1. Заполнить README.md
В файле `README.md` в первой строке заменить ФИО и группу на свои:
`Иванов Иван Иванович, группа 221341, вариант 8, лабораторная №1`

## Шаг 2. Проверить проект локально
```bash
cd mtp-lab1-variant8
python main.py
python -m unittest discover -s tests -v
```

## Шаг 3. Создать репозитории на GitHub
1. Создать пустой репозиторий `mtp-lab1-libmath` (без README, без .gitignore).
2. Создать пустой репозиторий `mtp-lab1-variant8` (без README, без .gitignore).

## Шаг 4. Опубликовать подмодуль
```bash
cd mtp-lab1-libmath
git remote add origin https://github.com/USERNAME/mtp-lab1-libmath.git
git branch -M main
git push -u origin main
```

## Шаг 5. Опубликовать основной проект
```bash
cd ../mtp-lab1-variant8
git remote add origin https://github.com/USERNAME/mtp-lab1-variant8.git
# (если origin уже есть: git remote set-url origin <url>)
git branch -M main
git push -u origin main
git push --all && git push --tags
```

## Шаг 6. Обновить ссылку на подмодуль
В `https://github.com/USERNAME/mtp-lab1-libmath` уже есть код. В основном репозитории
подмодуль указывает на этот URL — можно сказать git синхронизировать настройки:
```bash
git submodule sync
```

## Шаг 7. Клонирование чужих репозиториев (Средн.10)
```bash
git clone https://github.com/<любой-публичный-репозиторий>.git
cd <репозиторий>
git log --oneline --graph --decorate
git shortlog -sn
```

## Шаг 8. Сдать боту
Отправить боту отдельным сообщением **ссылку на репозиторий**:
`https://github.com/USERNAME/mtp-lab1-variant8`
Через 1–3 минуты придёт вердикт: «повышенная», «средняя» или «не принята».
