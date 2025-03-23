def check_string_length(string, length=5):
    if len(string) > length :
        print(f"Длина {string} строки достаточная")
    else:
        print(f"Строка {string} слишком короткая")
check_string_length("Python")
check_string_length("Hi")