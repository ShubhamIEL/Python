a = int(input("Enter First no"))
b = int(input("Enter Second no"))
print("a = ", a)
print("b = ", b)

# First way to solve
# a, b = b, a
# print(" After Swap a = ", a)
# print("After Swap b = ", b)

# Second way to solve
# a = a ^ b
# b = b ^ a
# a = a ^ b
# print(" After Swap a = ", a)
# print("After Swap b = ", b)

# Third way to solve
a = a + b
b = a - b
a = a - b
print(" After Swap a = ", a)
print("After Swap b = ", b)
