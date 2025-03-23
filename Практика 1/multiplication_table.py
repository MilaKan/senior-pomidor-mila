def multiplication_table(n):
    print(f"Таблица умножения для числа {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

number=int(input("Введите число для умножения: "))
multiplication_table(number)
