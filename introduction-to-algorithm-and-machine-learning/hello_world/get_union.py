"""Return the union of 2 arrays with no repeated element"""

def get_union(array1, array2):
    """
    Returns an array consiting of the elements that are either in array1 or array2
    """

    union = array1 + array2
    result = []

    for element in union:
        if element not in result:
            result.append(element)

    return result

a1 = [1, 2, 3, 4, 5, 6, 6]
a2 = [6, 7, 8, 9, 10, 11, 12]

b1 = get_union(a1, a2)
print(b1)