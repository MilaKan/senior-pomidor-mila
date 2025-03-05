def get_test_cases_per_week():
    days_of_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    test_cases = []
    for day in days_of_week:
        while True:
            try:
                cases = int(input(F"Введите количество выполненных тест-кейсов за {day}:"))
                if cases < 0:
                    print("Количество тест-кейсов не может быть 0. Попробуйте снова.")
                else:
                    test_cases.append(cases)
                    break
            except ValueError:
                print("Пожалуйста, введите целое число.")

    return test_cases

def calculate_weekly_stats(test_cases):
    total_cases = sum(test_cases)
    average_cases = total_cases / len(test_cases)
    return total_cases, average_cases

def main():
    print("Введите количество выполненных тест-кейсов за каждый день недели:")
    weekly_test_cases = get_test_cases_per_week()
    total_cases, average_cases = calculate_weekly_stats(weekly_test_cases)
    print("\nКоличество тест-кейсов за неделю:")
    days_of_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    for day, cases in zip(days_of_week, weekly_test_cases):
        print(f"{day}: {cases} тест-кейсов")

    print(f"\nОбщее количество тест-кейсов за неделю: {total_cases}")
    print(f"Среднее количество тест-кейсов в день: {average_cases:.2f}")
    if average_cases < 10:
        print("Отличная работа!")
    else:
        print("Попробуйте улучшить результат.")
if __name__ == "__main__":
     main()

