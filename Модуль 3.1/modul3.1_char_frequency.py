def char_frequency(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
print(char_frequency("hello"))  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}

