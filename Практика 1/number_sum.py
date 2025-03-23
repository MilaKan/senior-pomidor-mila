def main():
    try:
        n = int(input("Введите число: "))
    except ValueError:
        print("Ошибка: Введите целое число.")
        return
    if n <= 0:
        print("Ошибка: Введите положительное число.")
        return

    numbers = list(range(1, n + 1))
    print("Числа:", " ".join(map(str, numbers)))

    total_sum = sum(numbers) 
    print("Сумма чисел:", total_sum)

if __name__ == "__main__":
    main()