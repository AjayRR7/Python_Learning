"""
Create a program using maths and f-Strings that tells
us how many days, weeks, months we have left if we live until 90 years old
"""

age = input("enter your age: ")


age_is_int = int(age)

years_remaining = 90 - age_is_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

#f-string
message = f"you have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."

print(message)