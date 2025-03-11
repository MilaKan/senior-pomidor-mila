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


def print_diamond(rows):
    for i in range(rows):
        print("*" * (2 * i + 1))
    for i in range(rows - 2, -1, -1):
        print("*" * (2 * i + 1))

#print_diamond(10)
'''
text = "Hello World!"
print(text.lower())       # hello world!
print(text.upper())       # HELLO WORLD!
print(text.capitalize())  # Hello world!
print(text.title())       # Hello World!
'''

def greet(name):
    """
    Эта функция принимает имя пользователя
    и выводит приветственное сообщение.
    """
    print(f"Hello, {name}!")

#help(greet)  # Выводит описание функции

#numbers = [1, 2, 3, 2, 4]
#print(numbers.index(2))    # 1
#print(numbers.count(2))    # 2
#numbers = [x for x in range(1, 6)]
#print(numbers)  # [1, 2, 3, 4, 5]

#numbers = [x * 2 for x in range(1, 6)]
#print(numbers)  # [2, 4, 6, 8, 10]

#Преобразование строк в верхний регистр
#words = ["hello", "world", "python"]
#uppercase_words = [word.upper() for word in words]
#print(uppercase_words)  # ['HELLO', 'WORLD', 'PYTHON']


#Создадим список строк, длина которых больше 3:
#words = ["apple", "banana", "kiwi", "pear"]
#filtered_words = [word for word in words if len(word) > 3]
#print(filtered_words)  # ['apple', 'banana','kiwi', 'pear']

#numbers = [x**2 for x in range(10)  if x % 2 == 0]
#print(numbers)

#numbers = [-3, -2, -1, 0, 1, 2, 3]
#result = [x if x >= 0 else 0 for x in numbers]
#print(result)  # [0, 0, 0, 0, 1, 2, 3]
#Создадим список, где каждое число классифицируется как "чётное" или "нечётное":
#numbers = [1, 2, 3, 4, 5]
#result = ["чётное" if x % 2 ==0 else "не чётное" for x in numbers]
#print(result)

#numbers = [1, 2, 3, 4, 5]
#result = [x for x in numbers if x % 2 != 0]  # Только чётные числа
#print(result)  # [2, 4]
'''
#Метод pop() удаляет элемент по ключу и возвращает его значение.
my_dict = {"a": 1, "b": 2, "c": 3}
removed_value = my_dict.pop("b")
print(removed_value)  # 2
print(my_dict)     # {'a': 1, 'c': 3}
'''
my_set = {1, 2, 3, 4, 5}
my_set.remove(4)  # {1, 2, 3, 5}
my_set.discard(6)  # Ничего не происходит, так как 6 отсутствует
#removed_element = my_set.pop()  # Удаляет произвольный элемент
print(my_set)  # Например, 1