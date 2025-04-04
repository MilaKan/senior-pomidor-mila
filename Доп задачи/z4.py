def digitize(n):
    return [int(d) for d in str(n)[::-1]]
print(digitize(35231))   # => [1,3,2,5,3]
print(digitize(0))
print(digitize(23582357))  # => [7,5,3,2,8,5,3,2]