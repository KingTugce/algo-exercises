#Given a string after every y add an ! and after every s add a period and make every w and g capital
#Make a Function that takes a string as input and returns the adjusted string.
s="Hey welcome to doing whiteboard problems get prepared to figure our a problem on the fly"
#output= Hey! Welcome to doinG Whiteboard problems. Get prepared to fiGure our a problem on the fly!
# In [2]:
def new_string(string):
    new = ""
    for letter in string:
        if letter == "y":
            new += letter + "!"
        elif letter == "s":
            new += letter + "."
        elif letter == "w" or letter == "g":
            new += letter.upper()
        else:
            new += letter
    return new

new_string(s)#Given a string after every y add an ! and after every s add a period and make every w and g capital
#Make a Function that takes a string as input and returns the adjusted string.
s="Hey welcome to doing whiteboard problems get prepared to figure our a problem on the fly"
#output= Hey! Welcome to doinG Whiteboard problems. Get prepared to fiGure our a problem on the fly!

def new_string(string):
    new = ""
    for letter in string:
        if letter == "y":
            new += letter + "!"
        elif letter == "s":
            new += letter + "."
        elif letter == "w" or letter == "g":
            new += letter.upper()
        else:
            new += letter
    return new

new_string(s)