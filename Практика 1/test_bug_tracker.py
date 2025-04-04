bug_tracker= {"Анна": 3, "Иван": 5, "Дмитрий": 7}
print("Исходные данные:", bug_tracker)
name = input("Введите Имя тестировщика: ")
if name in bug_tracker:
    bug_tracker[name] += 1
else:
    bug_tracker[name] = 1
print("Обновленные данные:", bug_tracker)