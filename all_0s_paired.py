# For a given list of digits 0 to 9, 
# return a list with the same digits in the same order, 
# but with all 0s paired. 
# Pairing two 0s generates one 0 at the location of the first one.
# input: [0, 1, 0, 2]
# paired: ^-----^
#     -> [0, 1,   2]
#   kept: ^

# input: [0, 1, 0, 0]
# paired: ^-----^
#     -> [0, 1,    0]
#   kept: ^        ^
# Ex: [1,0,1,0,2,0,0,3,0]) would Output : [1,0,1,2,0,3,0]
# Ex: [1,0,1,0,2,0,0,3,0] would Output:  [1,0,1,2,0,3,0]

test_digits = [1,0,1,0,2,0,0,3,0]

def pair_zeros(digits):
  output = []
  zero_count = 0
  for num in digits:
    if num == 0 and zero_count == 0:
      output.append(num)
      zero_count += 1
    elif num == 0 and zero_count == 1:
      zero_count -= 1
    else:
      output.append(num)
  return output

print("OUT OF PLACE:")
print(test_digits)
print(pair_zeros(test_digits))
print(test_digits)

print('=========================')


def pair_zeros_inplace(digits):
  i = 0
  while i < len(digits):
    if digits[i] != 0:
      i += 1
    else:
      i += 1
      while i < len(digits):
        if digits[i] == 0:
          digits.pop(i)
          break
        i += 1
  return digits

print('IN PLACE:')
print(test_digits)
print(pair_zeros_inplace(test_digits))
print(test_digits)