def create_bug_reports():
    """
    Создаёт список из 7 баг-репортов.
    """
    bug_reports = [
        {"description": "Ошибка 1", "severity": "High"},
        {"description": "Ошибка 2", "severity": "Medium"},
        {"description": "Ошибка 3", "severity": "Low"},
        {"description": "Ошибка 4", "severity": "High"},
        {"description": "Ошибка 5", "severity": "Medium"},
        {"description": "Ошибка 6", "severity": "Low"},
        {"description": "Ошибка 7", "severity": "High"},
    ]
    return bug_reports


def filter_bugs(bug_reports, severity):
    """
    Фильтрует баги по указанному приоритету.
    """
    filtered_bugs = [bug for bug in bug_reports if bug["severity"].lower() == severity.lower()]
    return filtered_bugs


def main():
    """
    Основная функция программы.
    """
    # Создаём список баг-репортов
    bug_reports = create_bug_reports()

    # Запрашиваем у пользователя приоритет
    severity_levels = ["High", "Medium", "Low"]
    severity = input("Введите приоритет для фильтрации (High/Medium/Low): ").strip().capitalize()

    # Проверяем корректность ввода
    if severity not in severity_levels:
        print("Некорректный приоритет. Допустимые значения: High, Medium, Low.")
        return

    # Фильтруем баги
    filtered_bugs = filter_bugs(bug_reports, severity)

    # Выводим результат
    if filtered_bugs:
        print(f"\nБаги с приоритетом '{severity}':")
        for bug in filtered_bugs:
            print(f"Описание: {bug['description']}, Приоритет: {bug['severity']}")
    else:
        print(f"\nБагов с приоритетом '{severity}' не найдено.")


if __name__ == "__main__":
    main()