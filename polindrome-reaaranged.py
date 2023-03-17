#Given a string return True if the string can be rearranged to make a palindrome
#a palindrome can be spelled the same forwards and backward

# Input
s1="aabbcc"
# Output
# True

# Input
s2="aabebcc"
# Output
# True

# Input
s3="racecar"
# Output
# True

# Input
s4="abcd"
# Output
# False

# Input
s5="aaabbbcc"
# Output
# False

def is_pal(s1):
    

    if s1 == s1[::-1]:
        return True
    
    x = list(s1)
    letters = {}
    for letter in x:
        if letter in letters.keys():
            letters[letter] += 1
        else:
            letters[letter] = 1


    odd_letters = 0
    for k,v in letters.items():
        if v % 2 != 0:
            odd_letters += 1
    
    if len(s1) % 2 == 0 and odd_letters == 0:
        return True 
    elif len(s1) % 2 != 0 and odd_letters == 1:
        return True
    else:
        return False         

print(is_pal(s4))