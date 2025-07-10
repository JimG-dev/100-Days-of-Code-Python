# ### If/else
#
# print("Welcome to the Rollercoaster!")
#
# height = int(input("What's your height? \n"))
#
# if height >= 120:
#     print("You can ride!!")
# else:
#     print("No ride for you!!")

### Modulos

# number = int(input("Insert a number: \n"))
#
# if number % 2 == 0:
#     print("This is an even number")
# else:
#     print("Not an even number, pal!")
#
#

print("Welcome to the Rollercoaster!")

height = int(input("What's your height? \n"))

if height >= 120:

    age = int(input("How old are you?\n"))

    if age > 18:
        print("You pay $12")

    elif age >= 12:
        print("You pay $7")

    else:
        print("You pay $5")


else:
    print("You're not tall enough, friendo.")