def is_even(number):
    status = "чётным" if number % 2 == 0 else "нечётным"
    print(f"Число {number} является {status}")
is_even(14)