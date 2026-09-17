# """Return an array consisting of the elements that are in two arrays"""

# def get_intersection(array1, array2):
#     """
#     Returns an array consisting of the elements that are in both array1 and array2.
#     The output array does not contain any repated element
#     """
#     result = []

#     if array1 == array2:
#         for lst in array1:
#             if lst not in result:
#                 result.append(lst)

#     else:
#         for list1 in array1:
#             for list2 in array2:
#                 if list1 == list2 and list1 not in result:
#                     result.append(list1)

#     return result

"""Return an array consisting of the elements that are in two arrays"""

def get_intersection(array1, array2):
    """
    Returns an array consisting of the elements that are in both array1 and array2.
    The output array does not contain any repated element
    """
    result = []

    if array1 == array2:
        for lst in array1:
            if lst not in result:
                result.append(lst)

    else:
        for list1 in array1:
            if list1 in array2 and list1 not in result:
                result.append(list1)
            # for list2 in array2:
            #     if list1 == list2 and list1 not in result:
            #         result.append(list1)

    return result
test1 = ['M', 'a', 'k', 'i', 's', 'e']
test2 = ['P', 'e', 'a', 'k']

t3 = [2, 4, 4, 6]
t1 = [1, 3, 3]
t5 = [2, 4, 4, 6]
common = get_intersection(test1, test2)

n_common = get_intersection(t3, t5)

print(common)
# print(i*2 for i in t1)
print(2*t1)
print(f' this is {n_common}')
# print(['a', 'c', 't', '1'] == ['a', 'c', 't', '1'])

# name = ['a', 'bee', 'b', 'k']
# let = 'be'
# print(let not in name)