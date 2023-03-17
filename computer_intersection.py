"""
Compute Intersection:  Given two arrays, write 
a function to compute their intersection.
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:
Each element in the result must be unique.
The result can be in any order.
"""
nums1 = [4,9,5] 
nums2 = [9,4,9,8,4]

nums3 = [1,2,2,1]
nums4 = [2,2]

def intersect(list1, list2):
    set1 = set(list1)
    set2 = set(list2) 
    return set1.intersection(set2)

print(intersect(nums3, nums4))


#or, Vincent's answer:
def intersections():
    return list(set(filter(lambda x : True if x in nums2 else False, nums1)))

#or, from Terrell:
def intersectZ(nums1, nums2):
    return list(set(nums1).intersection(nums2))