# Minimum Index Sum of Two Lists
# Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.
# You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.
 
# Example 1:
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
# Output: ["Shogun"]
# Explanation: The only restaurant they both like is "Shogun".
 
# Example 2:
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
# Output: ["Shogun"]
# Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
 
# Example 3:
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
# Output: ["KFC","Burger King","Tapioca Express","Shogun"]
 
# Example 4:
# Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KNN","KFC","Burger King","Tapioca Express","Shogun"]
# Output: ["KFC","Burger King","Tapioca Express","Shogun"]
 
# Example 5:
# Input: list1 = ["KFC"], list2 = ["KFC"]
# Output: ["KFC"]

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
def output_item(arr_1, arr_2):
    output = {}
    for i in arr_1:
        if arr_1[i] in arr_2:
            output[i] = (arr_1.index(i) + arr_2.index(i))
    minval = min(output.values())
    return [x for x, y in output.items() if y == minval] 
print(output_item(list1, list2))


# def place_picker(partner_1, partner_2):
# 2	    total_list = []
# 3	    
# 4	    p1_dict = {partner_1[i]: i for i in range(len(partner_1))}
# 5	    
# 6	    
# 7	    for j in range(len(partner_2)):
# 8	        if partner_2[j] in p1_dict:
# 9	            total_list.append((partner_2[j],j+p1_dict[partner_2[j]]))
# 10	    
# 11	    if total_list:
# 12	        total_list.sort(key = lambda x: x[1])
# 13	        
# 14	        equals = list(filter(lambda x: x[0] if x[1] == total_list[0][1] else False,total_list))
# 15	        return equals[0][0]
# 16	    else:
# 17	        return "no matches in lists"

