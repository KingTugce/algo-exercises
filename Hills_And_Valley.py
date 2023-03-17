# -----------------
# Hills and Valleys
# -----------------
# ​
# An avid hiker keeps meticulous records of their hikes. 
# During the last hike that took exactly Steps, for every step it was noted 
# if it was an uphill, U , or a downhill, D step. Hikes always start and end at sea level, 
# and each step up or down represents a 1 unit change in altitude. We define the following terms:
# ​
# A mountain is a sequence of consecutive steps above sea level, starting with a step up 
# from sea level and ending with a step down to sea level.
# ​
# A valley is a sequence of consecutive steps below sea level, 
# starting with a step down from sea level and ending with a step up to sea level.
# ​
# Given the sequence of up and down steps during a hike, 
# find and print the number of valleys walked through.
# ​
# | Example:
# |
# | Steps = 8
# | Path = "DDUUUUDD"
# ​
# The hiker first enters a valley  units deep. 
# Then they climb out and up onto a mountain  units high. 
# Finally, the hiker returns to sea level and ends the hike.
# ​
# ​
# ​
# ​
# Function Description
# --------------------
# ​
# Complete the countingValleys function in the editor below.
# ​
# countingValleys has the following parameter(s):
# ​
# - int steps: the number of steps on the hike
# - string path: a string describing the path
# ​
#  Returns
#  -------
# - int: the number of valleys traversed
# ​
#  Input Format
# ​
#  The first line contains an integer , the number of steps in the hike.
#  The second line contains a single string path, of steps characters that describe the path.
# ​
# ​
# Sample Input
# ​
# 8
# UDDDUDUU
# ​
# Sample Output
# ​
# 1
# Explanation
# ​
# If we represent _ as sea level, a step up as /, and a step down as \, the hike can be drawn as:
# ​
# _/\      _
#    \    /
#     \/\/
# The hiker enters and leaves one valley.
# ​
# ​
# Ss
# ------------
# The Function
# ------------
# def CountingValleys(steps, path):
# Collapse


# def hill_and_vally(s):
#     d=[x1-x0 for x0,x1 in zip(s,s[1:]) if x1!=x0]
#     return 2+sum(d0*d1<0 for d0,d1 in zip(d,d[1:]))

def CountingValleys(steps, path):
    level = 0
    valley = 0
    for i in range(len(path)):
        if path[i] == "U" and level == 0:
            level += 1
            valley += 1
        elif path[i] == "D":
            level -= 1
        elif path[i] == "U":
            level += 1
    return valley

print(CountingValleys(8,""))