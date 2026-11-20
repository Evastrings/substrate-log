"""Uses Newton raphson method to approximate the nth root of a to desired level of precision"""

def derivative(x, n):
    return (n * (x ** (n - 1)))

def function_x(x, a, n):
    return (x ** n) - a

def newton_step(x_guess, a, n):
    derivative_at_guess = derivative(x_guess, n)

    if derivative_at_guess == 0:
        raise ValueError("Derivative is Zero")
    result = (x_guess * derivative_at_guess - function_x(x_guess, a, n)) / derivative_at_guess
    return result

def calc_root_newton_raphson(a, n, precision):
    """
    returns the approxiamtion of n_th root of a to desired precision
    """
    if not all(isinstance(val, int) for val in [a, n]):
        return "a and n must be integer"
    if not isinstance(precision, float):
        return "Precision must be float"
    if a == 1 and n != 0:
        return 1

    if a < 0 and n % 2 == 0:
        raise ValueError("no real roots")
    if a >= 1:
        old_guess = a
    elif a > 0:
        old_guess = 1
    else:
        old_guess = -1

    new_guess = newton_step(old_guess, a, n)

    while(abs(new_guess - old_guess) > precision):
        old_guess = new_guess
        new_guess = newton_step(old_guess, a, n)

    return new_guess


test = calc_root_newton_raphson(100, 2, 1e-6)

print(test)

# print(" === NEWTON RAPHSON BEGINS HERE ===")
# old_guess = 2
# precision = 1e-6

# def func_of_x(x):
#     result = (x ** 3) - 2
#     return result

# def f_prime_of_x(x):
#     result = 3 * (x ** 2)
#     return result

# def tangent_line_formula(x_guess):
#     result = (x_guess * f_prime_of_x(x_guess) - func_of_x(x_guess)) / f_prime_of_x(x_guess)
#     return result

# print(tangent_line_formula(old_guess))

# new_guess = tangent_line_formula(old_guess)

# while(abs(new_guess - old_guess) > precision):
#     old_guess = new_guess
#     new_guess = tangent_line_formula(old_guess)

# print(f"This is new_guess {new_guess}")

# print(round(new_guess, 6))