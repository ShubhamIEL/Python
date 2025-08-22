# # name = input("enter our name : ")
# # print(len(name))

# # str = "hi ,$ uhd $$$ ihih $"
# # print(str.count("$"))

# # str = "hii Shubham"
# # print(str[4: 9])

# movies = []

# movies.append(input("enter your 1st movie :"))
# movies.append(input("enter your 2nd movie :"))
# movies.append(input("enter your 3rd movie :"))

# print(movies)

# list1 = [1, 2, 3, 2, 1]
# list2 = list1.copy()
# list2.reverse()
# list2 = list1[::-1]  # slicing method

# print(list2 == list1)

tuple = ("C", "D", "A", "A", "B", "B", "A")
list1 = []
# print(tuple.count("A"))
# list1 = list(tuple)
# list1.sort()
# print(list1)
for i in tuple:
    list1.append(i)
list1.sort()
print(list1)
