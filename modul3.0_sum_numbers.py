def sum_numbers():
    try:
        n = int(input("Введите число: "))
    except ValueError:
        print("Ошибка: Введите целое число.")
        return
    if n <= 0:
        print("Ошибка: Введите положительное число.")
        return
    result = 0
    for i in range(1, n+1):
        result += i

    print(f"Сумма чисел от 1 до {n}: {result}")
    return result
sum_numbers()
