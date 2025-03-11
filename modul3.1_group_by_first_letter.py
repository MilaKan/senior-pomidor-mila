def group_by_first_letter(strings):
    groups = {}
    for s in strings:
        first_letter = s[0].lower()
        if first_letter in groups:
            groups[first_letter].append(s)
        else:
            groups[first_letter]= [s]
    return groups
strings = ["apple", "apricot", "banana", "blueberry", "cherry"]
print(group_by_first_letter(strings))
# {"a": ["apple", "apricot"], "b": ["banana", "blueberry"], "c": ["cherry"]}