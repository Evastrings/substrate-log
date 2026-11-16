# print(False == False)
digits = [1, 2, 3, 4]
square = []

def is_valid(sqr):
    if sqr == [[2, 1], [3, 4]]:
        return True

# for i in digits:
#     square = []
#     square.append([i])
#     for j in digits:
#         if i == j:
#             continue
#         square = []
#         square.append([i, j])
#         for k in digits:
#             if i == k or j == k:
#                 continue
#             square = []
#             square.append([i, j])
#             square.append([k])
#             for l in digits:
#                 if i == l or j == l or k == l:
#                     continue
#                 square= []
#                 square.append([i, j])
#                 square.append([k, l])

#                 if is_valid(square):
#                     print(square)
#                     break

# print("====LATEST SQUARE")
# print(square)
# print(len(square))
# me = []
# i = 9

# me.append([i])
# print(me)

def sum_row(rowss):
    sum = 0

    for i in rowss:
        sum += i
    return sum

def is_valid_magic_sqaure(square):
    col_1 = [square[0][0], square[1][0], square[2][0]]
    col_2 = [square[0][1], square[1][1], square[2][1]]
    col_3 = [square[0][2], square[1][2], square[2][2]]

    diag_1 = [square[0][0], square[1][1], square[2][2]]
    diag_2 = [square[0][2], square[1][1], square[2][0]]

    return sum_row(square[0]) == sum_row(square[1]) == sum_row(square[2]) == sum_row(col_1) == sum_row(col_2) == sum_row(col_3) == sum_row(diag_1) == sum_row(diag_2) == 15
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
square = []

for a in digits:
    square = []
    square.append([a])
    for b in digits:
        if a == b:
            continue
        square = []
        square.append([a, b])
        for c in digits:
            if a == c or b == c:
                continue
            square = []
            square.append([a, b, c])
            for d in digits:
                if a == d or b == d or c == d:
                    continue
                square = []
                square.append([a, b, c])
                square.append([d])
                for e in digits:
                    if a == e or b == e or c == e or d == e:
                        continue
                    square = []
                    square.append([a, b, c])
                    square.append([d, e])
                    for f in digits:
                        if a == f or b == f or c == f or d == f or e == f:
                            continue
                        square = []
                        square.append([a, b, c])
                        square.append([d, e, f])
                        for g in digits:
                            if a == g or b == g or c == g or d == g or e == g or f == g:
                                continue
                            square = []
                            square.append([a, b, c])
                            square.append([d, e, f])
                            square.append([g])
                            for h in digits:
                                if a == h or b == h or c == h or d == h or e == h or f == h or g == h:
                                    continue
                                square = []
                                square.append([a, b, c])
                                square.append([d, e, f])
                                square.append([g, h])
                                for i in digits:
                                    if a == i or b == i or c == i or d == i or e == i or f == i or g == i or h == i:
                                        continue
                                    square = []
                                    square.append([a, b, c])
                                    square.append([d, e, f])
                                    square.append([g, h, i])

                                    if is_valid_magic_sqaure(square):
                                        print(square)
#                 if is_valid(square):
#                     print(square)

# print(sum([1, 2, 3, 4, 5]))
# # j_ = 9
