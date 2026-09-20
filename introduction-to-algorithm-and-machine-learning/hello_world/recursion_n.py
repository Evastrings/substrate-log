def double_then_add_one(n):
    
    if not isinstance(n, int):
        return 'Enter an integer'
    if n <= 0:
        return []
    if n == 1:
        return [3]

    previous_list = double_then_add_one(n - 1)

    last_term = previous_list[-1]

    next_term = last_term * 2 + 1

    return previous_list + [next_term]


# for i in range(1, 9):
#     print(double_then_add_one(i))

print(double_then_add_one(8))
