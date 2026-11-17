"""Estimating roots via bisection search and Newton raphson method"""

# print(1.375 - 1.3125)

# print(round(2/3, 6))

#estimate cube root of 2

def f_of_x(x_val):
    result = (x_val ** 3) - 2
    return result

upper_bound = 3
lower_bound = 1

# print(f_of_x(2))
precision = 1e-6

print(precision * 1000)

midpoint = (upper_bound + lower_bound) / 2
prev_midpoint = 0

while ((abs(upper_bound - lower_bound) / 2) > precision):
    
    # print("===I AM IN WHILE LOOP ===")
    if f_of_x(midpoint) >= 0:
        upper_bound = midpoint
    else:
        lower_bound = midpoint
    
    prev_midpoint = midpoint
    midpoint = (upper_bound + lower_bound) / 2

print(f"The cuberoot of 2 is {round(midpoint, 6)}")

print(f"raw midpoint -> {midpoint}")

print(midpoint ** 3)

# NEWTON RAPHSON SCRIPT
print(" === NEWTON RAPHSON BEGINS HERE ===")
old_guess = 2
precision = 1e-6

def func_of_x(x):
    result = (x ** 3) - 2
    return result

def f_prime_of_x(x):
    result = 3 * (x ** 2)
    return result

def tangent_line_formula(x_guess):
    result = (x_guess * f_prime_of_x(x_guess) - func_of_x(x_guess)) / f_prime_of_x(x_guess)
    return result

print(tangent_line_formula(old_guess))

new_guess = tangent_line_formula(old_guess)

while(abs(new_guess - old_guess) > precision):
    old_guess = new_guess
    new_guess = tangent_line_formula(old_guess)

print(f"This is new_guess {new_guess}")

print(round(new_guess, 6))

# print(1 - None)
