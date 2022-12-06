#ticketing with NESTED_IF

height = int(input("Enter your height in cm: "))
age = int(input("Enter your age: "))

if height > 120:
    print("you are eligible")

    if age >= 18:
        print("you just pay 12$")

    else:
        print("you just pay 7$")

else:
    print("you are not eligible")
