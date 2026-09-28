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
    result = [[]]

    for current_list in lists:
        tmp_points = []

        for item in current_list:
            for point in result:
                tmp_points.append(point + [item])
        result = tmp_points

    return result





sets = [['a'], [1, 2, 3], ['Y', 'Z']]
sc = calc_cartesian_product(sets)
print(sc)
print(calc_cartesian_product([['a', 'b'], ['c', 'd']]))
# print(calc_cartesian_product([4]))
print(calc_cartesian_product([]))
# print(calc_cartesian_product(1))
print(calc_cartesian_product([[], [1, 2]]))
print(calc_cartesian_product([[1, 2], []]))
print(not[])

# points = [[]]

# for sett in sets:

#     tmp = []
#     for member in sett:
#         for point in points:
#             tmp.append(point + [member])

#     points = tmp

# print(points)
# points = []
# tmp_points = []
# final_points = []

# for sett in sets:
#     if len(points) < 1:
#         points.append(sett)
#     else:
#         print(f"Value of tmp_points {tmp_points}")
#         print(f"set in this loop is {sett}")
#         for member in sett:
#             length = len(points)
#             for point in range(length):
#                 point_list = points[point] + [member]
#                 # tmp_points = []
#                 print(f"Value of point list is {point_list}")
#                 points.append(point_list)
#                 print(f"===VALUE OF PINT {points}")

# print(tmp_points)

# def calc_cartesian_product(item):
#     pass





# point = [['a', 1], ['a', 2], ['a', 3]]
# testing = ['X', 'Y']
# copy = []

# for i in testing:
#     for j in point:
#         vvv = j + [i]
#     # vv = point + [i]
#     copy.append(vvv)

# print(copy)


# tests = [['a', 'b'], ['c', 'd']]
# range_test = list.copy(tests)

# points = []
# my_ans = [['a', 'c'], ['a', 'd'], ['b', 'c'], ['b', 'd']]

# for i, test in enumerate(range_test):
#     point = []
#     print(f"This is the value of POINTS at the beginning of each loop {points}")
#     points[i].append()
#     for j, val in enumerate(test):
#         point.append(j)

#     points.append(point)

# print(f" FINAL VALUE OF POINTS LIST {points}")
# orig = [['a'], [1, 4, 5, 7], ['this is me, vsn'], 3]

# new = [[]]
# new2 = list.copy(orig)
# for tt in orig:
#     new.append(tt)

# print(f" Jsyk, this is new 2 used with list.copy {new2}")
# print("btw ORIG AND NRIG ARE REFERENCES, NEW AND NEW2 AND COPIED LIST")

# print(f" Jsyk, this is ORIG{orig}")
# nrig = orig
# print(f" Jsyk, this is also NRIG{nrig}")

# nrig[2] = ['sin arc bishop']
# print(f" Jsyk, this is the LATEST ORIGINAL{orig}")
# print(f" Jsyk, this is THE LATEST NRIG{nrig}")

# new[1] = ['Petra']
# print(f" Jsyk, this is LATES NEW{new}")

# new2[2] = ['Emilia-TAN']
# print(f" Jsyk, this is the LATEST NEW2{new2}")

# for i, mem in enumerate(new):
#     print(f" new{i} is {mem}")


