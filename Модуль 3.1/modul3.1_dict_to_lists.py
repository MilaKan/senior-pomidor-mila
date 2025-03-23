def dict_to_lists(my_dict):
    keys_list = list(my_dict.keys())
    value_list = list(my_dict.values())
    return keys_list , value_list

my_dict = {"a": 1, "b": 2, "c": 3}
print(dict_to_lists(my_dict))  # (["a", "b", "c"], [1, 2, 3])