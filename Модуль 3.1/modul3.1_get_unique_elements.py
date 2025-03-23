def get_unique_elements(lst):
    my_list = lst
    set_list = set(my_list)
    return set_list
print(get_unique_elements([1, 2, 2, 3, 4, 4, 4, 5]))  # [1, 2, 3, 4, 5]