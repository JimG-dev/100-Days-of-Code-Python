# ### Print can be augmented with \n for line breaks - as with JS
#
# print("Hello World!\nHello World!\nHello World!")
#
# ### Concatenation is the same as JavaScript really.
#
# print("Hello " + "James")
#
# ### Printing can also directly print the result of an input as below (Use vars instead though, obvs).
#
# print(input("What's your name?"))

# ### Variables
#
# user_name = input("What's your name?\n")
# username_length = len(user_name)
#
# ### Len
#
# print(f"Your name is {user_name}, which is {username_length} characters in length.")

### Project: Band Name Generator

print("Welcome to the Band Name Generator.")

user_city = input("What's the name of the city you grew up in?\n")

user_pet_name = input("What's your pet's name?\n")

print(f"Your band name could be {user_city} {user_pet_name}")