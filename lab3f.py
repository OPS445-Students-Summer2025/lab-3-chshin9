#!/usr/bin/env python3

# Place my_list below this comment (before the function definitions)
my_list = [ 1, 2, 3, 4, 5 ]

def add_item_to_list(ordered_list):
    temp = ordered_list[-1] 
    ordered_list.append(temp + 1)

def remove_items_from_list(ordered_list, items_to_remove):
    copy_list = ordered_list.copy()
    for items in copy_list:
        if items in items_to_remove:
            ordered_list.remove(items)

# Main code
if __name__ == '__main__':
    print(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    print(my_list)
    remove_items_from_list(my_list, [1,5,6])
    print(my_list)
