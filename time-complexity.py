# def intersection(arr1, arr2):
#     arr3 = []
#     for element1 in arr1:
#         for element2 in arr2:
#             if element1 == element2:
#                 arr3.append(element2)
#     return arr3


def intersection(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)
    return list(set1 & set2)


arr1 = [0, 1, 4, 5, 8]
arr2 = [0, 2, 7, 9, 4]

print(intersection(arr1, arr2))
