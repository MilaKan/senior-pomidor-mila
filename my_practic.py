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

#
# # Пример использования:
# car1 = Car.from_string("Toyota-Corolla")
# print(f"Бренд: {car1.brand}, Модель: {car1.model}")
# print(f"Всего автомобилей: {Car.car_count}")

my_dict = {"a": 1, "b": 2, "c": 3}
for key , value in my_dict.items():
    print(key , value)