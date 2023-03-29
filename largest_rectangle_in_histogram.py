# 10- Largest rectangle in histogram:

def largest_rectangle(heights):
    max_area = 0
    for i in range(len(heights)):
        left = i
        while left-1 >= 0 and heights[left-1] >= heights[i]:
            left -= 1
        right = i
        while right+1 < len(heights) and heights[right+1] >= heights[i]:
            right += 1
        max_area = max(max_area, heights[i]*(right-left+1))
    return max_area

def rec(heights, low, high):
    if low > high:
        return 0
    elif low == high:
        return heights[low]
    else:
        minh = min(heights[low:high+1])
        pos_min = heights.index(minh, low, high+1)
        from_left = rec(heights, low, pos_min-1)
        from_right = rec(heights, pos_min+1, high)
        return max(from_left, from_right, minh*(high-low+1))
