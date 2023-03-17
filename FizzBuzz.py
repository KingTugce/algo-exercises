# Fizz Buzz 
# Given a random number as an input to a function, return "FIZZ" if the number 
# is even and "BUZZ" if the number is odd

# Example Input: 1
# Example Output: 'BUZZ'
# Example Input: 1002
# Example Output: 'FIZZ'

def FizzBizz(nums):
    for num in nums:
        if num %2 == 0:
            print("Fizz")
        else:
            print("Buzz")
print(FizzBizz([0,7,9,2,30,4,5,1]))
