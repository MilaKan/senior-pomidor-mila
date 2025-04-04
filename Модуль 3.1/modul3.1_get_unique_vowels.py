def get_unique_vowels(s):
    vowels = "aeiou"
    unique_vowels = set()

    for char in s:
        if char in vowels:
            unique_vowels.add(char.lower())
    return unique_vowels
print(get_unique_vowels("Hello World"))  # {'e', 'o'}