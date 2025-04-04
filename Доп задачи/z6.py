def filter_number(lst):
    return [x for x in lst if isinstance(x,int)]

print(filter_number([1, 2, 'a', 'b'])) #[1, 2, 'a', 'b'] = > [1, 2]
print(filter_number([1, 'a', 'b', 0, 15]))     # [1, 'a', 'b', 0, 15] => [1, 0, 15]
print(filter_number([1, 2, 'a', 'b']))     # [1, 2, 'a', 'b'] => [1, 2]