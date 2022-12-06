#job is to build an automatic pizza order program.
"""
Based on a user's order, work out their final bill.
Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25
Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: + $1
"""

print("welcome to python pizza delivery's")
size = input("Which size do you wants? S, M, or L :\n")
add_pepperoni = input("Do you want pepperoni? Y or N :\n")
extra_cheese = input('Do you wants extra cheese? Y or N :\n')
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill +=20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1

print(f"your final bill is ${bill}")
