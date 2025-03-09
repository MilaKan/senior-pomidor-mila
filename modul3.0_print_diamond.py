def print_diamond(rows):
    for i in range(rows):
        print("*" * (i + 1))
    for i in range(rows - 1, 0, -1):
        print("*" * i)

print_diamond(4)