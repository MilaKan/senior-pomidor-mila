def find_min(numbers):
    min_number = numbers[0]
    for number in numbers:
        if number < min_number:
            min_number = number
    print(f"Минимальное число в списке {numbers}: {min_number}")
    return min_number
find_min([3, 1, 4, 1, 5])