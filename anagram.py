#Given two strings, return true if they are anagrams of each other, and false otherwise.
#An anagram is a word, phrase, or name formed by rearranging the letters of another.
s1 = "anagram"
t1 = "nagaram"
# Output:
# True
s2 = "rat"
t2 = "car"
#Output:
# False

def is_anagram(string1, string2):
    return len(string1) == len(string2) and set(string1) == set(string2)

# def is_anagram(s_1, s_2):
#     list_1 = sorted(s_1)
#     list_2 = sorted(s_2)
#     if list_1 == list_2:
#         return True
#     else:
#         return False
print(is_anagram(s1,t1))
print(is_anagram(s2,t2))