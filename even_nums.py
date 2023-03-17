# Find Even numbers
# Create a function that, given a list as a parameter, finds the even numbers inside the list. The function should then return a list.
# Example:
# Input: [2, 7, 10, 11, 12]
# Output: [2, 10, 12]

# def find_evens[even in even for even in lst if even %2 == 0]

def find_evens(lst):
    even_numbers = []
    for numbers in lst:
        if numbers % 2 == 0:
            even_numbers.append(numbers)
    return even_numbers

print(find_evens([2, 7, 10, 11, 12]))

# def evens(a_list):
#     evens_dict = {}
#     for nums in a_list:
#         if nums % 2 == 0:
#             evens_dict.add(nums)
#     return evens

# print(evens([2,3,5,88,6,2,]))

