def where_do_we_eat(my_options, your_options):
    our_options = {}
    your_options_set = set(your_options)
    for restaurant in my_options:
        if restaurant in your_options_set:
            index_sum = my_options.index(restaurant) + your_options.index(restaurant)
            our_options[restaurant] = index_sum
    min_index_sum = min(our_options.values())
    return [key for key, value in our_options.items() if value == min_index_sum]



list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
list3 = ["Shogun","Tapioca Express","Burger King","KFC"] 
list4 = ["KFC","Shogun","Burger King"]
list5 = ["Shogun","Tapioca Express","Burger King","KFC"]
list6 = ["KFC","Burger King","Tapioca Express","Shogun"]
list7 = ["Shogun","Tapioca Express","Burger King","KFC"] 
list8 = ["KNN","KFC","Burger King","Tapioca Express","Shogun"]
list9 = ["KFC"] 
list10 = ["KFC"]
print(where_do_we_eat(list1, list2)) # Output: ["Shogun"]
print(where_do_we_eat(list3, list4)) # Output: ["Shogun"]
print(where_do_we_eat(list5, list6)) # Output: ["KFC","Burger King","Tapioca Express","Shogun"]
print(where_do_we_eat(list7, list8)) # Output: ["KFC","Burger King","Tapioca Express","Shogun"]
print(where_do_we_eat(list9, list10)) # Output: ["KFC"]