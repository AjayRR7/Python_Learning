#program that calculates the Body Mass Index (BMI) from a user's weight and height

height = input("enter your height in m: ")
weight = input("enter your weight: ")


bmi = int(weight) / float(height) ** 2

bmi_in_int = int(bmi)

print(bmi_in_int)

