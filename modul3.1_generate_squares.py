def generate_squares(n):
    numbers = [x ** 2 for x in range(1,n+1)]
    print(numbers)  # [1, 4, 9, 16, 25]
generate_squares(5)