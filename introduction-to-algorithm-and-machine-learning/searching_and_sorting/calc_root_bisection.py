"""Calculates the roots of a number using bisection method"""

def calc_root_bisection(a, n, precision):
    if not all(isinstance(val, (int, float)) for val in [a, n]):
        return "Invalid Integer"
    if not isinstance(precision, float):
        return "Precision must be float"

    if a == 1 and n != 0:
        return a
    if n > 0 and n < 1:
        return a ** (1 / n)
    if a > 0 and n >= 1:
        lower = 0
        upper = 1

        while((upper ** n) < a):
            upper *= 2

    elif a < 0 and n % 2 == 1:
        lower = -1
        upper = 0

        while((lower ** n) > a):
            lower *= 2
    else:
        return "No real roots"

    # if ((upper ** n) == a):
        # return upper

        # print("== START OF MIDPOINT ===")
        # print(f"I am upper: {upper}")
        # print(f"I am lower {lower}")
        
        # midpoint = (lower + upper) / 2
        # print(f" This is midpoint: {midpoint}")

        # count = 0

        # print(abs(upper - lower) / 2 < precision)

    while(abs(upper - lower) / 2 > precision):
        midpoint = (lower + upper) / 2
        if ((midpoint ** n) == a):
            return midpoint
        # count += 1
        # print(f" THE VALUE OF UPPER IN BEGINING OF {count}th ABS LOOP: {upper}, this is LOWER:{lower}, this is MIDPOINT: {midpoint}")
        if ((midpoint ** n) - a) >= 0:
            upper = midpoint
        else:
            lower = midpoint
        # print(f" THE VALUE OF UPPER IN BEGINING OF {count}th ABS LOOP: {upper}, this is LOWER:{lower}, this is MIDPOINT: {midpoint}")
        # midpoint = (lower + upper) / 2
        # print(f" THIS IS NEW MIDPOINT AT LOOP END: {midpoint}")
    return round(midpoint, 6)
        # return midpoint

    #     pass
    # else:
    #     return "No real root"
    

ft = 1e-6
# print(type(ft))
# print(str(ft))
# print(len(str(ft)))

print(calc_root_bisection(8, 3, ft))
