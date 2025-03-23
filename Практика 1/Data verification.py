def get_test_cases_per_day():
    while True:
        try:
            cases = int(input(f"Введите количество выполненных тест-кейсов за день : "))
            if cases < 0:
                print("Количество тест-кейсов не может быть 0. Попробуйте снова.")
            else:
                return cases
        except ValueError:
            print("Некорректный ввод. Введите положительное число.")

def main():
    cases = get_test_cases_per_day()
    if cases > 10:
        print("Отличная работа!")
    else:
        print("Попробуйте улучшить результат.")
if __name__ == "__main__":
     main()