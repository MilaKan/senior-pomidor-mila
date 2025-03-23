def collect_bug_reports():
    bug_reports = []
    while True:
        description = input("Введите описание бага (или 'exit' для завершения): ")
        if description.lower() == 'exit':
            break
        severity_levels = ['blocker', 'critical', 'high', 'medium', 'low']
        severity = input("Введите уровень критичности (blocker/critical/high/medium/low): ").lower()
        while severity not in severity_levels:
            print("Некорректный уровень критичности. Попробуйте снова.")
            severity = input("Введите уровень критичности (blocker/critical/high/medium/low): ").lower()

        status_option = ['открыт', 'в работе', 'исправлен', 'отклонен', 'закрыт']
        status = input("Введите статус бага (открыт/в работе/исправлен/отклонен/закрыт): ").lower()
        while status not in status_option:
            print("Некорректный статус. Попробуйте снова.")
            status = input("Введите статус бага (открыт/в работе/исправлен/отклонен/закрыт): ").lower()
        if severity == 'low':
            print("Баг с низким приоритетом (low) не добавлен.")
        else:
            bug_report = {
            'description': description,
            'severity': severity,
            'status': status
        }
            bug_reports.append(bug_report)
            print("Баг успешно добавлен!\n")
    return bug_reports


def analyze_bug_reports(bug_reports):
    severity_levels = ['blocker', 'critical', 'high', 'medium', 'low']
    severity_counts = {level: 0 for level in severity_levels}

    status_options = ['открыт', 'в работе', 'исправлен', 'отклонен', 'закрыт']
    status_counts = {status: 0 for status in status_options}

    for report in bug_reports:
        severity_counts[report['severity']] += 1
        status_counts[report['status']] += 1

    return severity_counts, status_counts

def main():
    print("Сбор отчётов об ошибках (багах). Для завершения введите 'exit'.")
    bug_reports = collect_bug_reports()
    severity_counts, status_counts = analyze_bug_reports(bug_reports)

    print("\nСтатистика по уровням критичности:")
    for severity, count in severity_counts.items():
        print(f"{severity.capitalize()}: {count} багов")

    print("\nСтатистика по статусам:")
    for status, count in status_counts.items():
        print(f"{status.capitalize()}: {count} багов")


if __name__ == "__main__":
    main()