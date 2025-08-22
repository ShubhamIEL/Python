# print(type(5))

# for c in "Python":
#     print(c)

# for x in [1, 2, 3, 4]:
#     print(x)

# no = 101
# while no > 0:
#     print(no)
#     no //= 2

# command = ""
# while command != "q":
#     command = input(">")
#     print("ECHO", command)

# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)

count = 0
for i in range(1, 10):
    if i % 2 == 0:
        print(i)
        count += 1
print(f"Total {count} Even numbers ")
