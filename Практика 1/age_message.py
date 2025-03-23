from datetime import datetime
def calculate_age(birth_year):
    current_year = datetime.now().year
    age = current_year - birth_year
    return age

def main():
    try:
        birth_year = int(input("Введите ваш год рождения: "))
        current_year = datetime.now().year
        if birth_year > current_year:
            age = calculate_age(birth_year)
            print("Ошибка: Год рождения не может быть больше текущего года.")
        else:
            age = calculate_age(birth_year)
            if age < 18:
                print("Вы еще молоды, учеба — ваш путь!")
            elif 18 <= age < 65:
                print("Отличный возраст для карьерного роста!")
            else:
                print("Пора наслаждаться заслуженным отдыхом!")
    except ValueError:
            print("Ошибка: Введите корректный год рождения (целое число).")
if __name__ == "__main__":
    main()