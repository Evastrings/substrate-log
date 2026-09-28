"""Calculate the cartesian product points"""

def calc_cartesian_product(lists: list):
    """
    Create an array that will contain all the points in the cartesian product.
    """
    if not isinstance(lists, list):
        raise TypeError("Input must be a list of lists")
    if not all(isinstance(lst, list) for lst in lists):
        raise TypeError("Every element must be a list")
    
    if not lists:
        return [[]]
    for lst2 in lists:
        if not lst2:
            return []
    result = [[]]

    for current_list in lists:
        tmp_points = []

        for item in current_list:
            for point in result:
                tmp_points.append(point + [item])
        result = tmp_points

    return result







