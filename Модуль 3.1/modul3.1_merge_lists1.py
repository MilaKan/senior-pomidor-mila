def merge_lists(list1, list2):
    merge_set = set(list1).union(set(list2))
    merge_lists = list(merge_set)
    return merge_lists
print(merge_lists([1, 2, 3], [3, 4, 5]))  # [1, 2, 3, 4, 5]