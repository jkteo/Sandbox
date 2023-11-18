password = input("Please enter the password: ")
min_length = 2

if len(password) >= min_length:
    print(len(password) * "*")
else:
    password = input("Please enter the password: ")