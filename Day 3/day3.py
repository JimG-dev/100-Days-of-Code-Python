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
total = 0

if height >= 120:

    age = int(input("How old are you?\n"))

    if age > 18:
        print("Adult tickets are $12.")
        total = 12

    elif age >= 12:
        print("Youth tickets are $7.")
        total = 7

    else:
        print("Child tickets are $5.")
        total  = 5

    photo = input("Do you want to have a photo taken? Type y for Yes or n for No.\n")

    if photo == "y":
        total += 3

    print(f"Your total comes to ${total}.")




else:
    print("You're not tall enough, friendo.")