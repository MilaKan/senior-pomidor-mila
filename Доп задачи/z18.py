def list(nums):
    return len(nums) != len(set(nums))

print(list([1, 2, 3, 1]))
print(list([1, 2, 3, 4]))