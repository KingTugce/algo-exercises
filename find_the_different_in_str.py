# find the difference in a string you are given two strings s and t. String t
# is generated by random shuffling string s and then add one more letter at a
# random position. Return the letter that was added to t.

# Example 1 Input: s ="abcd", t="abcde" Output: "e" Explanation 'e' is the letter
# that was added. Example2: Input: s="",t="y" Output:"y"Example 3: Input s ="a",
# t="aa" Output:"a" Example4: Input s="ae", t="aea" Output:"a"

s = "ta"
t = "tabb"

def find_difference(str1,str2):
    for letter in str2:
        if str1.count(letter) != str2.count(letter):
            return letter


print(find_difference(s , t))
