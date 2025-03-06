def main():
    my_list = [4, 7, 9, 2, 5]
    my_tuple = (4, 7, 9, 2, 5)
    print("Исходный список: ", my_list)
    print("Исходный кортеж: ", my_tuple)
    my_list[1] = 10
    print("Измененный список: ", my_list)
    try:
        my_tuple[1] = 10
    except TypeError :
        print("Ошибка: Кортеж нельзя изменить!")

    my_list.append(6)
    print("Добавленный элемент в список: ", my_list)
    try:
        my_tuple.append(6)
    except AttributeError:
        print("Ошибка: В кортеж нельзя добавить элемент!")
if __name__ == "__main__":
    main()