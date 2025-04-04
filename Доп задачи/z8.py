def sort(num_list):
    numbers=[]
    for item in num_list:
        try:
            numbers.append(int(item))
        except (ValueError, TypeError):
            continue
    return sorted(numbers)
print(sort([1 , "2" ,"3",98,32,"73",12,-6 ]))