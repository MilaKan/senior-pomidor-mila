#
# def greet(name):
#     print(f"Привет {name}!")

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

'''
def print_diamond(rows):
    for i in range(rows):
        print("*" * (2 * i + 1))
    for i in range(rows - 2, -1, -1):
        print("*" * (2 * i + 1))

#print_diamond(10)
'''
# text = "Hello World!"
# print(text.lower())       # hello world!
# print(text.upper())       # HELLO WORLD!
# print(text.capitalize())  # Hello world!
# print(text.title())       # Hello World!
'''


def greet(name):
    """
    Эта функция принимает имя пользователя
    и выводит приветственное сообщение.
    """
    print(f"Hello, {name}!")
'''
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
# my_set = {1, 2, 3, 4, 5}
# my_set.remove(4)  # {1, 2, 3, 5}
# my_set.discard(6)  # Ничего не происходит, так как 6 отсутствует
# #removed_element = my_set.pop()  # Удаляет произвольный элемент
# print(my_set)  # Например, 1

# def sum_l(num):
#     total = sum(num)
#     print(total)
# sum_l([1, 2, 3, 4, 5])

# def min_l(numbers):
#     minx=max(numbers)
#     print(minx)
# min_l([10, 20, 30, 40, 50])

# def uniqu(numbers):
#     uniqu_set = set(numbers)
#     uniqu_list = uniqu_set
#     return uniqu_list
# print(uniqu([1, 2, 2, 3, 4, 4, 5]))

# def reverses(numbers):
#     numbers.sort()
#     return numbers
#
# print(reverses([1, 2, 3, 4, 5]))

# fruits = ["яблоко", "банан", "апельсин", "банан", "банан"]
# lens = len(fruits)
# print(lens)

# items = ["яблоко", "банан", "яблоко", "апельсин", "банан", "яблоко"]
# frequency = {}
# for item in items:
#     if item in frequency:
#         frequency[item] += 1
#     else:
#         frequency[item] = 1
# for key , value in frequency.items():
#      print(f"{key}: {value}")
# text = "apple,banana,cherry"
# fruits = text.split(",")
# print(fruits) # ["apple", "banana", "cherry"]
#
# joined_text = " ".join(fruits)
# print(joined_text) # "apple-banana-cherry"
'''

class Car:
    def __init__(self, brand, model, speed=0):
        self.brand = brand # Марка автомобиля
        self.model = model  # Модель автомобиля
        self.speed = speed  # Текущая скорость

    def accelerate(self, increment):
        self.speed += increment
        print(f"{self.brand} {self.model} ускоряется. Текущая скорость: {self.speed} км/ч.")

    def brake(self, decrement):
        self.speed = max(0, self.speed - decrement)
        print(f"{self.brand} {self.model} замедляется. Текущая скорость: {self.speed} км/ч.")


    def display_info(self):
        print(f"Автомобиль: {self.brand} {self.model}, Скорость: {self.speed} км/ч")

# car1 = Car("Toyota", "Corolla")
# car1.accelerate(80)
# car1.brake(10)
# car1.display_info()

class ElectricCar(Car):
    def __init__(self, brand, model, battery_level, speed=0):
        super().__init__(brand, model, speed)
        self.battery_level = battery_level # Уровень заряда батареи


    def charge(self, amount):
        self.battery_level = min(100, self.battery_level + amount)
        print(f"Батарея заряжена до {self.battery_level}%")


    def display_info(self):
# Переопределение метода для вывода дополнительной информации
        print(f"Электромобиль: {self.brand} {self.model}, Скорость: {self.speed} км/ч, Заряд: {self.battery_level}%")
'''
# Создание объекта класса ElectricCar:
# e_car = ElectricCar("Tesla", "Model 3", battery_level=50)
# e_car.accelerate(40)
# e_car.charge(30)
# e_car.display_info()



# class GasolineCar(Car):
#     def start_engine(self):
#         print(f"{self.brand} {self.model}: Двигатель бензинового автомобиля запущен.")
#
#
# class ElectricCar(Car):
#     def start_engine(self):
#         print(f"{self.brand} {self.model}: Электродвигатель запущен, тихий старт!")
#
#
# # Создание объектов разных классов:
# cars = [GasolineCar("Ford", "Focus"), ElectricCar("Nissan", "Leaf")]
#
#
# # Вне зависимости от типа автомобиля, вызываем метод start_engine:
# for car in cars:
#     car.start_engine()
'''
class Car:
    def __init__(self, brand, model, fuel_level=0):
        self.brand = brand
        self.model = model
        self.__fuel_level = fuel_level # Приватный атрибут, не доступный напрямую

    def refuel(self, amount):
        if amount > 0:
            self.__fuel_level += amount
        if self.__fuel_level > 100: # Предположим, что уровень топлива не может превышать 100%
            self.__fuel_level = 100
            print(f"{self.brand} {self.model}: Добавлено {amount}% топлива. Текущий уровень: {self.__fuel_level}%.")
        else:
            print("Сумма для заправки должна быть положительной!")

    def drive(self, consumption):
        if consumption > self.__fuel_level:
            print(f"{self.brand} {self.model}: Недостаточно топлива для поездки!")
        else:
            self.__fuel_level -= consumption
            print(f"{self.brand} {self.model}: Поездка завершена. Осталось {self.__fuel_level}% топлива.")
    def get_fuel_level(self):
        return self.__fuel_level


# # Пример использования:
# my_car = Car("Honda", "Civic", fuel_level=50)
# my_car.refuel(80)# Закидываем 30% топлива
# my_car.drive(60) # Расходуем 60% топлива на поездку
# print(f"Текущий уровень топлива: {my_car.get_fuel_level()}%")

def decorator(func):
    def wrapper():
        print("Начало выполнения функции")
        func()
        print("Конец выполнения функции")
    return wrapper

@decorator
def greet():
    print("Привет!")

#greet()

class Car:
    car_count = 0 # Классный атрибут для подсчёта созданных автомобилей


    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.car_count += 1


    @classmethod
    def from_string(cls, car_str):
        brand, model = car_str.split('-')
        return cls(brand, model)
'''
#
# # Пример использования:
# car1 = Car.from_string("Toyota-Corolla")
# print(f"Бренд: {car1.brand}, Модель: {car1.model}")
# print(f"Всего автомобилей: {Car.car_count}")

# my_dict = {"a": 1, "b": 2, "c": 3}
# for key , value in my_dict.items():
#     print(key , value)

    # Напишите
    # программу, которая выводит числа от
    # 1 до  n(включительно), но:
    #
    # Если
    # число
    # делится
    # на
    # 3, вместо
    # числа
    # выведите
    # "Fizz".
    # Если
    # число
    # делится
    # на
    # 5, вместо
    # числа
    # выведите
    # "Buzz".
    # Если
    # число
    # делится
    # и
    # на
    # 3, и
    # на
    # 5, выведите
    # "FizzBuzz".
    # В
    # остальных
    # случаях
    # выведите
    # само
    # число.
    #
    # Пример
    # входных
    # данных:
    # n = 15
    #
    # Пример
    # выходных
    # данных:
    # 1
    # 2
    # Fizz
    # 4
    # Buzz
    # Fizz
    # 7
    # 8
    # Fizz
    # Buzz
    # 11
    # Fizz
    # 13
    # 14
    # FizzBuzz

# def calculate(n):
#     for i in range(1,n+1):
#         if i % 3 == 0 and i % 5 == 0:
#             print("Fizzbuzz")
#         elif i % 3 ==0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)
#
# calculate(15)
'''
def text(str):
    string = str.split(",") # hello world!
    print(string)
    joined_str = "-".join(string)
    print(joined_str)
# text("Hello, World!")

def text1 (str1):
    new_str = str1.replace("Hello", "Happy")
    print(new_str)
'''
# text1("Hello, World!")

# text = "   "
# index = text.isspace()
# print(index)  # Вывод: 8


# text = "Привет, мир!"
# result = text[::-1]
# print(result)  # Вывод: "Привет"

# text = "He said, \"Hello!\""
# print(text)  # He said, "Hello!"

# text = """Это пример многострочной строки.
# Она может содержать несколько строк текста,
# и все они будут сохранены в переменной."""
# print(text)

# def is_anagram(s1, s2):
#     s1 = s1.replace(" "," ").lower()
#     s2 = s2.replace(" "," ").lower()
#     return sorted(s1) == sorted(s2)
#
# print(is_anagram("listen", "silent"))  # True
# print(is_anagram("hello", "world"))  # False
# import re
# def is_palindrome(s):
#     cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
#     return cleaned_string == cleaned_string[::-1]
# print(is_palindrome("A man, a plan, a canal: Panama")) # True
# print(is_palindrome("racecar"))                         # True
# print(is_palindrome("hello"))                         False

# def longest_word(s):
#     word = s.split()
#     s_long = max(word, key = len)
#     return s_long
#
# print(longest_word("In the middle of a vast desert, an extraordinary adventure awaits"))  # "extraordinary”

# def format_phone_number(digits):
#     format_number = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
#     return format_number
# print(format_phone_number("1234567890"))  # "(123) 456-7890”

# def remove_duplicates(s):
#     result = []
#     for char in s:
#         if char not in result:
#             result.append(char)
#     return ''.join(result)
#
# print(remove_duplicates("programming"))  # "progamin”

# numbers = [1, 2, 3]
# numbers.append(5)
# numbers.insert(3 , 4)
# numbers.extend([8, 9])
# numbers.remove(1)
# removed = numbers.pop(0)
# print(numbers)
# numbers = [1, 2, 3,6,9,11,10]
# total = sum(numbers)
# print(total)

# squares = [x * 2 for x in range(1, 6+1) if x % 2 == 0]
# print(squares)  # Вывод: [1, 4, 9, 16, 25]

# words = ["hello", "world", "python","lo"]
# filtered_words = [word for word in words if len(word) >=3]
# print(filtered_words)  # ['HELLO', 'WORLD', 'PYTHON']

# numbers = [x*2 for x in range(10) if x % 2 == 0]
# print(numbers)  # [0, 4, 16, 36, 64]

# numbers = [-3, -2, -1, 0, 1, 2, 3]
# result = [x if x >= 0 else 1 for x in numbers]
# print(result)  # [0, 0, 0, 0, 1, 2, 3]

# def remove_duplicates(lst):
#     my_list = set(lst)
#     return my_list
# print(remove_duplicates([1, 2, 2, 3, 4, 4]))  # [1, 2, 3, 4]

# def generate_squares(n):
#     numbers =[x**2 for x in range(1,5+1)]
#     return numbers
# print(generate_squares(5))  # [1, 4, 9, 16, 25]

# def merge_lists(list1, list2):
#     merge_set = set(list1).union(set(list2))
#     merge_lists = list(merge_set)
#     return merge_lists
#
# print(merge_lists([1, 2, 3], [3, 4, 5]))  # [1, 2, 3, 4, 5]

# def is_sorted(lst):
#     return lst == sorted(lst)
#
# print(is_sorted([1, 2, 3, 4, 5]))  # True
# print(is_sorted([1, 3, 2, 4, 5]))  # False

# def merge_lists(list1, list2):
#     lists = [x+y for x ,y in zip(list1,list2)]
#     return lists
# print(merge_lists([1, 2, 3], [4, 5, 6]))  # [5, 7, 9]

# my_dict = {"a": 1, "b": 2, "c": 3}
# for value in my_dict.values():
#     print(value)

# my_dict = {"a": 1, "b": 2}
# del my_dict["b"]
# print(my_dict.get("a"))  # Вывод: Not Available

# my_dict = {"a": 1, "b": 2}
# removed_value =  my_dict.pop("b")
# print(removed_value)
# print(my_dict)
#
# my_dict = {"a": 1, "b": 2}
# my_dict.clear()
# print(my_dict)

# numbers = [1, 2, 3, 4, 5]
# squares_dict = {x: x ** 2 for x in numbers if x % 2 == 0}
# print(squares_dict)

# words = ["apple", "banana", "cherry"]
# length_dict = {word: len(word) for word in words}
# print(length_dict)

# dict1 = {"a": 1, "b": 2}
# dict2 = {"b": 3, "c": 4}
# dict1.update(dict2)
# print(dict1)

# def char_frequency(s):
#     frequency = {}
#     for char in s:
#         if char in frequency:
#             frequency[char] += 1
#         else:
#             frequency[char] = 1
#     return frequency
#
# print(char_frequency("hello"))

# def merge_dicts(dict1, dict2):
#     dict1.update(dict2)
#     return dict1
# dict1 = {"a": 1, "b": 2}
# dict2 = {"b": 3, "c": 4}
# print(merge_dicts(dict1, dict2))  # {"a": 1, "b": 5, "c": 4}

# def dict_to_lists(my_dict):
#     list_keys = list(my_dict.keys())
#     list_values = list(my_dict.values())
#     return list_keys , list_values
# my_dict = {"a": 1, "b": 2, "c": 3}
# print(dict_to_lists(my_dict))  # (["a", "b", "c"], [1, 2, 3])

# def group_by_first_letter(strings):
#     groups = {}
#     for s in strings:
#         first_letter = s[0].lower()
#         if first_letter in groups:
#             groups[first_letter].append(s)
#         else:
#             groups[first_letter] = [s]
#     return groups
# strings = ["apple", "apricot", "banana", "blueberry", "cherry"]
# print(group_by_first_letter(strings))
#     # {"a": ["apple", "apricot"], "b": ["banana", "blueberry"], "c": ["cherry"]}

# def extract_subdict(my_dict, keys):
#     return {key:my_dict[key] for key in keys if key in my_dict}
#
# my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
# keys = ["a", "c"]
# print(extract_subdict(my_dict, keys))  # {"a": 1, "c": 3}

# class Car:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
#
#     def drive(self):  # Метод "ехать"
#         print(f"{self.brand} is driving!")
#
#     def stop(self):  # Метод "остановиться"
#         print(f"{self.brand} has stopped.")
#
# my_car = Car("Tesla", "red")
# my_car.drive()  # Вывод: Tesla is driving!
# my_car.stop()   # Вывод: Tesla has stopped.
"""
class Car:
    def __init__(self, brand, model, speed=0):
        self.brand = brand # Марка автомобиля
        self.model = model  # Модель автомобиля
        self.speed = speed  # Текущая скорость


    def accelerate(self, increment):
        self.speed += increment
        print(f"{self.brand} {self.model} ускоряется. Текущая скорость: {self.speed} км/ч.")


    def brake(self, decrement):
        self.speed = max(0, self.speed - decrement)
        print(f"{self.brand} {self.model} замедляется. Текущая скорость: {self.speed} км/ч.")


    def display_info(self):
        print(f"Автомобиль: {self.brand} {self.model}, Скорость: {self.speed} км/ч")

# # Создание объектов класса Car:
car1 = Car("Toyota", "Corolla")
car1.accelerate(30)
car1.brake(10)
car1.display_info()


class ElectricCar(Car):
    def __init__(self, brand, model, battery_level, speed=0):
        super().__init__(brand, model, speed)
        self.battery_level = battery_level # Уровень заряда батареи


    def charge(self, amount):
        self.battery_level = min(100, self.battery_level + amount)
        print(f"Батарея заряжена до {self.battery_level}%")


    def display_info(self):
    # Переопределение метода для вывода дополнительной информации
        print(f"Электромобиль: {self.brand} {self.model}, Скорость: {self.speed} км/ч, Заряд: {self.battery_level}%")

# Создание объекта класса ElectricCar:
e_car = ElectricCar("Tesla", "Model 3", battery_level=50)
e_car.accelerate(40)
e_car.charge(30)
e_car.display_info()

class GasolineCar(Car):
    def start_engine(self):
        print(f"{self.brand} {self.model}: Двигатель бензинового автомобиля запущен.")


class ElectricCar(Car):
    def start_engine(self):
        print(f"{self.brand} {self.model}: Электродвигатель запущен, тихий старт!")


# Создание объектов разных классов:
cars = [GasolineCar("Ford", "Focus"), ElectricCar("Nissan", "Leaf")]


# Вне зависимости от типа автомобиля, вызываем метод start_engine:
for car in cars:
    car.start_engine()
"""
"""
def decorator(func):
    def wrapper():
        print("Начало выполнения функции")
        func()
        print("Конец выполнения функции")
    return wrapper

@decorator
def greet():
    print("Привет!")

#greet()

def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat

@repeat(num_times=5)
def say_hello(name):
    print(f"Привет, {name}!")

#say_hello("Анна")

class Car:
    def __init__(self, brand, model, speed=0):
        self.brand = brand
        self.model = model
        self.__speed = speed # Приватный атрибут скорости


@property
def speed(self):
  '''Геттер для получения скорости автомобиля.'''
    return self.__speed


@speed.setter
def speed(self, value):
   '''Сеттер для установки скорости автомобиля с проверками.'''
    if value < 0:
        print("Ошибка: скорость не может быть отрицательной!")
    elif value > 300:
        print("Ошибка: превышено максимально допустимое значение скорости (300 км/ч)!")
    else:
        self.__speed = value


@speed.deleter
def speed(self):
    '''Делитер для удаления атрибута скорости.'''
    print("Свойство скорости удалено!")
    del self.__speed


def display_info(self):
    print(f"Автомобиль: {self.brand} {self.model}, Скорость: {self.__speed} км/ч")




# Пример использования:
car = Car("Toyota", "Corolla")


# Чтение значения скорости (вызывает getter)
print(f"Начальная скорость: {car.speed} км/ч")


# Установка нового значения скорости (вызывает setter)
car.speed = 150
print(f"Обновленная скорость: {car.speed} км/ч")


# Попытка установить некорректное значение (отрицательное)
car.speed = -20


# Попытка установить слишком высокую скорость
car.speed = 350


# Удаление свойства скорости (вызывает deleter)
del car.speed
"""

# Попытка обращения к удалённому свойству приведёт к ошибке, если его не восстановить
#print(car.speed) # Раскомментируйте эту строку для проверки
"""
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def service_check(self):
        # Метод имитирует проверку автомобиля в сервисе
        print(f"Проводится диагностика автомобиля {self.brand} {self.model}.")

    def __str__(self):
        return f"{self.brand} {self.model}"

class CarService:
    def __init__(self, car):
        self.car = car

    def __enter__(self):
        # Код, выполняющийся при входе в контекст
        print(f"Автомобиль {self.car} поступил в сервисное обслуживание.")
        return self.car  # возвращаем автомобиль для работы внутри блока with

    def __exit__(self, exc_type, exc_value, traceback):
        # Код, выполняющийся при выходе из контекста
        if exc_type:
            print(f"Во время обслуживания автомобиля {self.car} произошла ошибка: {exc_value}")
        print(f"Автомобиль {self.car} покидает сервисное обслуживание.")
        return False

# Пример использования контекстного менеджера:
my_car = Car("BMW", "X5")

# Используем контекстный менеджер для обслуживания автомобиля:
with CarService(my_car) as car_in_service:
    car_in_service.service_check()
    # Если требуется, можно сымитировать ошибку:
    # raise ValueError("Проблема с оборудованием диагностики")
"""
'''
from dataclasses import dataclass

@dataclass
class Car:
    brand: str
    model: str
    year: int
    speed: int = 0

    def accelerate(self, increment: int):
        """Увеличивает скорость автомобиля."""
        self.speed += increment
        print(f"{self.brand} {self.model} ускоряется до {self.speed} км/ч.")

    def brake(self, decrement: int):
        """Уменьшает скорость автомобиля, не опускаясь ниже 0."""
        self.speed = max(0, self.speed - decrement)
        print(f"{self.brand} {self.model} замедляется до {self.speed} км/ч.")

# Пример использования:
car = Car("Audi", "A4", 2022)
print(car)  # Автоматически использует сгенерированный __repr__
car.accelerate(50)
car.brake(20)
'''
'''
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"


class CarLot:
    def __init__(self, cars):
        self.cars = cars
        self.index = 0 # Индекс текущего автомобиля


    def __iter__(self):
 # Метод __iter__ возвращает итератор (в данном случае, сам объект)
        return self


    def __next__(self):
# Если еще есть автомобили, возвращаем следующий
        if self.index < len(self.cars):
            car = self.cars[self.index]
            self.index += 1
            return car
        else:
# Если автомобилей больше нет, останавливаем итерацию
            raise StopIteration


# Создадим несколько объектов Car:
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2019)
car3 = Car("Ford", "Mustang", 2021)


# Создаем автосалон, используя наш список автомобилей:
lot = CarLot([car1, car2, car3])


# Перебор автомобилей в автосалоне:
print("Автомобили в автосалоне:")
for car in lot:
    print(car)
'''
'''
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"


def car_factory(total):
    """
    Генератор, имитирующий производство автомобилей.
    total - общее количество автомобилей для производства.
    """
    for i in range(1, total + 1):
        # Создаем автомобиль с порядковым номером модели и динамическим годом выпуска
        yield Car("BrandX", f"Model-{i}", 2020 + i)


# Используем генератор для производства 5 автомобилей:
print("\nПроизводственная линия (генератор автомобилей):")
for car in car_factory(10):
    print(car)
    '''
'''
def  check_sign():
    num = int(input("Ввведите число: "))
    if num > 0 :
        print("Число является положительным!")
    elif num < 0:
        print("Число является отрицательным!")
    else:
        print("Число является нулём!")

#check_sign()

def longest_common_prefix(strs):
    if not strs:
        return ""  # Если массив пуст, возвращаем пустую строку

    # Находим длину самой короткой строки
    min_length = min(len(s) for s in strs)

    result = ""
    for i in range(min_length):
        current_char = strs[0][i]  # Берем символ из первой строки
        for s in strs:
            if s[i] != current_char:
                return result  # Если символы не совпадают, возвращаем результат
        result += current_char  # Добавляем символ к результату

    return result

# Пример использования
# strs1 = ["flower", "flow", "flight"]
# print(longest_common_prefix(strs1))  # Вывод: "fl"
#
# strs2 = ["dog", "racecar", "car"]
# print(longest_common_prefix(strs2))  # Вывод: ""
'''
