# Very simple, given an integer or a floating-point number, find its opposite.

# Examples:

# 1: -1
# 14: -14
# -34: 34

def solution(number):
    x = number - (number*2)
    return x
print(solution(5))