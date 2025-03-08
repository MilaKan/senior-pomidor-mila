def greet(name):
    print(f"Привет {name}!")

#greet("Анна")
#greet("Иван")
'''
def is_seven(number):
    number = int(number)
    try:
        if number % 2 ==0:
            return ("Ваше число чётное")
        else:
            return ("Ваше число не чётное")
    except ValueError:
        return "Ввести можно только целое число."
user_answer = (input("Введите целое число: "))
result = is_seven (user_answer)
print(result)
'''
'''
def numbers(a , b):
    return a + b
number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
result = numbers(number1,number2)
print(f"Cумма двух чисел: {result}")
'''
'''
def find_max(a, b , c):
    return max(a, b ,c)
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))
result = find_max (num1, num2, num3)
print(f"Наибольшее число: {result}")
'''
'''
def count_vowels(text):
    vowels = "Милана!"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count
user_input = input("Введите текст: ")
result = count_vowels(user_input)
print(result)
'''