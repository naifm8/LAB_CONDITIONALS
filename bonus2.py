user_name = input("Enter your name: ")
if len(user_name) > 2:
    print("The is valid")
else:
    print("Please enter more than tow characters")

user_email = input("Enter your email: ")
if "@gmail.com" in user_email and user_email.count("@") == 1:
    print("Email is valid")
else:
    print("Please enter a valid Gmail address")