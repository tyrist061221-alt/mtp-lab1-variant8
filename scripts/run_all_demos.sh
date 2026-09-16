#!/usr/bin/env bash
# Запуск демонстраций всех заданий варианта 8.
# Использование: bash scripts/run_all_demos.sh
set -u

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

STATUS=0
for TASK in sredn_4_second_commit sredn_8_github_remote sredn_10_clone_history \
            povysh_1_merge_conflict povysh_8_submodules; do
    echo "======================================================"
    echo ">>> Задание: $TASK"
    echo "======================================================"
    if python3 "tasks/$TASK.py"; then
        echo "-- РЕЗУЛЬТАТ: $TASK -> OK"
    else
        echo "-- РЕЗУЛЬТАТ: $TASK -> ОШИБКА"
        STATUS=1
    fi
    echo
done

echo "======================================================"
if [ "$STATUS" -eq 0 ]; then
    echo "Все демонстрации выполнены успешно."
else
    echo "Часть демонстраций завершилась с ошибкой."
fi
exit "$STATUS"
