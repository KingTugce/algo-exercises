# Ransom Note
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true

# def note(ransomNote,magazine):
#     for letters in ransomNote:
#         if ransomNote.count(letters) <= magazine.count(letters):
#             continue
#         else:
#             return False

#     return True

# print(note('aa','aab'))

from collections import Counter

def note(ransomNote, magazine):
    ransomCount = Counter(ransomNote) 
    magCount = Counter(magazine)
    
    for key,value in ransomCount.items(): # O(n)
        if magCount[key] and magCount[key] >= value:
            continue
        else:
            return False
    return True
    
note('aa','ab')
note('aac','aab')







