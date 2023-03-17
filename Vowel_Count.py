# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.

def getCount(sentence):
    vowels = 'aeiou'
    vowels_count = 0
    for char in sentence:
        if char.lower() in vowels:
            vowels_count += 1
    return vowels_count

# def get_vowel_count(a_string):
#     vowels = re.compile('[aeiou]')
#     return len(vowels.findall(a_string))

# get_vowel_count('hello_world')

def get_count(string):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel_count = 0
    for letter in string:
        if letter in vowels:
            vowel_count += 1
    return vowel_count


get_count('hello world')