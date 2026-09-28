"""Return an array consisting of the elements that are in two arrays"""

def get_intersection(array1, array2):
    """
    Returns an array consisting of the elements that are in both array1 and array2.
    The output array does not contain any repated element
    """
    result = []

    for list1 in array1:
        if list1 in array2 and list1 not in result:
            result.append(list1)

    return result

