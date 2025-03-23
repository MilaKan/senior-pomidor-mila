import re
def longest_word(s):
    words = re.findall(r'\b\w+\b', s)
    longest = max(words, key=len)
    return longest
print(longest_word("In the middle of a vast desert, an extraordinary adventure awaits")) # "extraordinary”