def get_middle(word):
    length = len(word)
    mid = length // 2
    if length % 2 == 0:
        return word[mid - 1: mid + 1]
    else:
        return word[mid]

print(get_middle("meet"))
print(get_middle("rudiment"))
print(get_middle("timber"))
print(get_middle("industry"))
print(get_middle("to"))
print(get_middle("procrastinate"))
print(get_middle("A"))