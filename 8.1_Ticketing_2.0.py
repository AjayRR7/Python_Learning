
print("welcome to the rollercoaster")
height = input("Enter your height in cm : ")
bill = 0

if height >= "120":
    print("yes, you can ride the rollercoaster")
    age = int(input("Enter your age: "))
    if age < 12:
        bill = 5
        print("child tickets are $5")
    elif age <= 18:
        bill = 7
        print("your ticket rate is $7")
    elif age >= 45 and age <= 55:
        print("you can ride for free")
    else:
        bill = 12
        print("adult tickets are $12")
    wants_photo = input("you wants your photo? Y or N: ")
    if wants_photo == "Y" or "y":
        bill += 3

    print(f"your final bill is {bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")

