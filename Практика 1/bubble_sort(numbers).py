def bubble_sort(numbers):
    n=len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers
numbers = [5, 2, 9, 1, 5, 6]
print(f"Исходный список: {numbers}")
sorted_numbers = bubble_sort(numbers)
print("Отсортированный список:", sorted_numbers)