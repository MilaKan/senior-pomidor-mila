def remove_duplicates(lst):
    my_list=lst
    my_set = set(my_list)
    return my_set

print(remove_duplicates([1, 2, 2, 3, 4, 4]))  # [1, 2, 3, 4]