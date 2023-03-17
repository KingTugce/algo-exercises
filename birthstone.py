#Write a function that prompts the user for their birth month and returns their birthstone.
#If they input an invalid month, tell them to try again

def zodiac():
    num = input("Hello! What is your birth month? Please enter the number of that month: ")

stones={
    1:"Garnet",
    2:"Amethyst",
    3:"Aquamarine",
    4:"Diamond",
    5:"Emerald",
    6:"Pearl",
    7:"Ruby",
    8:"Peridot",
    9:"Sapphire",
    10:"Opal",
    11:"Topaz",
    12:"Turquoise"
}


if num in stones:
    return stones[int(num)]

else:
    return "Please enter a valid number 1-12"

print(zodiac())