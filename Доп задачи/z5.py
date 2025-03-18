
def vowelss(string):
    vowels = "aeiou"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

print(vowelss("aeiou")) #"aeiou" => 5#"y" => 0
print(vowelss("bcdfghjklmnpqrstvwxz y")) #"bcdfghjklmnpqrstvwxz y" => 0
print(vowelss("abracadabra"))#"abracadabra" => 5

