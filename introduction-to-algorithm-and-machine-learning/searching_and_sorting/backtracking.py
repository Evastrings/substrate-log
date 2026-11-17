"""Solving magic squares via backtracking"""

def sum_row(rowss):
    sum_count = 0

    for i in rowss:
        sum_count += i
    return sum_count

def get_lines(square):
    return [
        square[0],
        square[1],
        square[2],

        [square[0][0], square[1][0], square[2][0]],
        [square[0][1], square[1][1], square[2][1]],
        [square[0][2], square[1][2], square[2][2]],

        [square[0][0], square[1][1], square[2][2]],
        [square[0][2], square[1][1], square[2][0]]
    ]

def is_valid_magic_square(square):
    for line in get_lines(square):
        if sum_row(line) != 15:
            return False
    return True

# BACK TRACKING EXERCISE
# def is_hopeless(squar_e):
#     """
#     returns True if a magic square is impossible with current numbers
#     """

#     lines = get_lines(squar_e)
#     # print(lines)

#     for line in lines:
#         if None not in line:
#             if sum_row(line) != 15:
#                 return True
#     return False
def is_hopeless(square):
    for line in get_lines(square):
        if None not in line and sum(line) != 15:
            return True
    return False


digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
square = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

for a in digits:
    square[0][0] = a
    for b in digits:
        if a == b:
            continue
        square[0][1] = b
        for c in digits:
            if a == c or b == c:
                continue
            square[0][2] = c
            square[1] = [None, None, None]
            square[2] = [None, None, None]
            if is_hopeless(square):
                continue
            for d in digits:
                if a == d or b == d or c == d:
                    continue
                square[1][0] = d
                for e in digits:
                    if a == e or b == e or c == e or d == e:
                        continue
                    square[1][1] = e
                    for f in digits:
                        if a == f or b == f or c == f or d == f or e == f:
                            continue
                        square[1][2] = f
                        square[2] = [None, None, None]
                        if is_hopeless(square):
                            continue
                        for g in digits:
                            if a == g or b == g or c == g or d == g or e == g or f == g:
                                continue
                            square[2][0] = g
                            square[2][1] = None
                            square[2][2] = None
                            if is_hopeless(square):
                                continue
                            for h in digits:
                                if a == h or b == h or c == h or d == h or e == h or f == h or g == h:
                                    continue
                                square[2][1] = h
                                square[2][2] = None
                                if is_hopeless(square):
                                    continue
                                for i in digits:
                                    if a == i or b == i or c == i or d == i or e == i or f == i or g == i or h == i:
                                        continue
                                    square[2][2] = i
                                    if is_hopeless(square):
                                        continue

                                    if is_valid_magic_square(square):
                                        print(square)
















# print(([[1, 2, None],[None, None, None],[5, 6, 4 ]]))

# # print(is_hopeless([[1, 2, None],[None, None, None],[5, 6, 4]]))

# w = [[1, 2, 3], [None, 4, 3], [4, 9, 2]]
# q = [[1, 2, None],[None, None, None],[5, 6, 4]]
# print(is_hopeless(w))

# print(is_hopeless(q))

# for row in square:
#         if None not in row:
#             if sum_row(row) != 15:
#                 return True
#         else:
#             return False
#             # return bool(None not in row and sum_row(row) != 15)
#     col_1 = [square[0][0], square[1][0], square[2][0]]
#     col_2 = [square[0][1], square[1][1], square[2][1]]
#     col_3 = [square[0][2], square[1][2], square[2][2]]

#     diag_1 = [square[0][0], square[1][1], square[2][2]]
#     diag_2 = [square[0][2], square[1][1], square[2][0]]
#     columns_and_diagonals = [col_1, col_2, col_3, diag_1, diag_2]

#     for array in columns_and_diagonals:
#         if None not in array and sum_row(array) != 15:
#             return True
#         else:
#             return False
#             # return bool(None not in array and sum_row(array) != 15)

# def is_hopeless(squar_e):
#     """
#     returns True if a magic square is impossible with current numbers
#     """

#     lines = get_lines(squar_e)
#     # print(lines)

#     for line in lines:
#         if None not in line:
#             if sum_row(line) != 15:
#                 return True
#         else:
#             return False

# def is_valid_magic_sqaure(square):
#     """
#     returns true if a square is a magic square
#     """
#     col_1 = [square[0][0], square[1][0], square[2][0]]
#     col_2 = [square[0][1], square[1][1], square[2][1]]
#     col_3 = [square[0][2], square[1][2], square[2][2]]

#     diag_1 = [square[0][0], square[1][1], square[2][2]]
#     diag_2 = [square[0][2], square[1][1], square[2][0]]

#     return sum_row(square[0]) == sum_row(square[1]) == sum_row(square[2]) == sum_row(col_1) == sum_row(col_2) == sum_row(col_3) == sum_row(diag_1) == sum_row(diag_2) == 15