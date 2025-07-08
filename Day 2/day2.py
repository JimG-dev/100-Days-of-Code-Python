# ### Dissecting strings - below grabs the first char
#
# print("Hello"[0])
#
# ### Below grabs the last chat - this is semi-dynamic
#
# print("Hello"[-1])
#

# ### Data Types
#
# print(type(123)) #int
#
# print(type("123")) #string
#
# print(type(True)) #boolean
#
# print(type(3.14)) #float
#
# ### Type Casting
#
# print(int("123")) #casts to int
#
# ### Challenge
#
# length_of_name = len(input("Enter your name:\n"))
#
# print(f"Number of letters in your name: {length_of_name}")

# ### Rounding to two decimal places | round(value, digits) |
#
# bmi = 84 / (1.65  ** 2)
#
# print(round(bmi, 2))

### Project: Tip Calculator

print("Welcome to the Tip Calculator!")

bill = float(input("What was the total bill amount?\n$"))
tip = float(input("How much tip would you like to give? 10, 12 or 15 percent?\n")) / 100
split_between = int(input("How many people to split the bill?\n"))

total_and_tip = bill + (bill * tip)

print(f"Each person should pay: ${round(total_and_tip / split_between, 2)}")


