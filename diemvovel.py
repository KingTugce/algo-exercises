# def disemvowel(troll_string):
#     vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
#     troll_list = list(troll_string)
#     for v in vowels:
#         while v in troll_list:
#             troll_list.remove(v)
#     return ''.join(troll_list)


# disemvowel('This website is for losers LOL!')
# ' m  trll lsr!'
# import re
# string = 'This website is for losers LOL!'

# re.sub(r"[aeiouAEIOU]",  "", string)

def disem_vowel(string):
    vowels = {"a","e","i","o","u"}
    liste = list(string)
    for v in vowels:
        while v in liste:
            liste.remove(v)
    return " ".join(liste)
disem_vowel('Hello World')
