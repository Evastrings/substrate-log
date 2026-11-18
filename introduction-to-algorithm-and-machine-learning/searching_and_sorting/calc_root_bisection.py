"""Calculates the roots of a number using bisection method"""

def calc_root_bisection(a, n, precision):
    """
    returns the nth root of a number using the numerical bisection method
    """
    if not all(isinstance(val, int) for val in [a, n]):
        return "a and n must be integer"
    if not isinstance(precision, float):
        return "Precision must be float"

    if a == 1 and n != 0:
        return 1
    
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

    midpoint = (lower + upper) / 2

    while(abs(upper - lower) / 2 > precision):
        if ((midpoint ** n) == a):
            return midpoint
        if ((midpoint ** n) - a) >= 0:
            upper = midpoint
        else:
            lower = midpoint
    return midpoint
    


