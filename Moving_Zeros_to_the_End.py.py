l = [1, 0, 1, 2, 0, 1, 3]
def move_zeros(array):
    l1 = []
    l2 = []
    for i in array:
        if i != 0 :
            l1.append(i)
        else: l2.append(i)
    return l1 + l2
print(move_zeros(l))
