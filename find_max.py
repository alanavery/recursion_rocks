# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# This function returns the largest number in a given array.

def find_max(l, largest_num=-float('inf')):
    if len(l) == 0:
        return largest_num
    if l[0] > largest_num:
        new_largest_num = l[0]
    else:
        new_largest_num = largest_num
    return find_max(l[1:], new_largest_num)


print(find_max([1, 4, 45, 6, -50, 10, 2]))
# => 45
