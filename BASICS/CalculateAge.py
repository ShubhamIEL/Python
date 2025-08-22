# from datetime import datetime, date


# user_input = input("Enter DOB (dd-mm-yyyy) : ")
# print(user_input)

# try:
#     birth_date = datetime.strptime(user_input, "%d-%m-%Y").date()
#     today = date.today()
#     age = (today.year - birth_date.year) - \
#         ((today.month, today.day) < (birth_date.month, birth_date.day))
#     print(f"Your Age is : {age}")

# except ValueError:
#     print("Invalid Date Format")


from datetime import datetime, date
from dateutil import parser

user_input = input(
    "Enter your birth date (any format, e.g. yyyy-mm-dd or dd/mm/yyyy): ")

try:
    birth_date = parser.parse(user_input)
    today = date.today()
    age = today.year - birth_date.year - \
        ((today.month, today.day) < (birth_date.month, birth_date.day))
    print(f"Your age is: {age}")
except:
    print("Invalid date format. Please try again.")
