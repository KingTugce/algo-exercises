# Max consecutive Nums:

# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Example 1:
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

# Example 2:
# Input: nums = [1,0,1,1,0,1]
# Output: 2


def find_con_max(arr):
    counter = 0
    max_count = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            counter += 1
            if counter > max_count: 
                max_count = counter
        else:
            counter = 0
    return max_count

print(find_con_max([1,0,1,1,1,0,1]))