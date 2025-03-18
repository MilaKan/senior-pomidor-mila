def multiples(x,n):
    return  [x*i for i in range(1, n+1)]

print(multiples(1,5))        # (1, 5) => [1, 2, 3, 4, 5])
print(multiples(3,5))       # (3, 5) => [3, 6, 9, 12, 15])
print(multiples(50,5))        # (50, 5) => [50, 100, 150, 200, 250])