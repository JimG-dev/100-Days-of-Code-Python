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

### Variables

name = input("What's your name?\n")
length = len(name)

### Len

print(f"Your name is {name}, which is {length} characters in length.")