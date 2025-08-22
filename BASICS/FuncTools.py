from functools import reduce

nums = [1, 2, 3, 4, 5]

# Map → square each element
squared = list(map(lambda x: x**2, nums))
print(squared)

# Filter → only even numbers
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

# Reduce → sum of all elements
sum_all = reduce(lambda x, y: x + y, nums)
print(sum_all)


def square(x): return x**2


print(square(5))  # 25
