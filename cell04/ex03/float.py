num = input("Give me a number: ")

if '.' in num:
    if float(num).is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
else:
    print("This number is an integer.")
