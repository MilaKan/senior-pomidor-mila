def calculator():
    numb1 = float(input("Введите первое число: "))
    operation = input("Введите опрерацию (+ , - , / ,*):")
    numb2 = float(input("Введите второе число: "))

    if operation  == "+":
        result = numb1+numb2
    elif operation == "-":
        result = numb1-numb2
    elif operation == "/":
        result = numb1 / numb2
    elif operation == "*":
        result = numb1 * numb2
    else:
        return "Ошибка: неизвестная операция!"
    return f"Результат: {result}"
print(calculator())

