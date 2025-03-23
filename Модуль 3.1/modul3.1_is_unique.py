def is_unique(s):
    return len(set(s)) == len(s)

print(is_unique("abcdef"))  # True
print(is_unique("hello"))  # False