"""Check whether an integer is prime"""

def is_prime(N):
    """
    Checks whether an interger N > 1 is prime by checking whether there exists 
    some n ∈ {2,3,4,...,⌊N/2⌋} such that n divides N.
    """
    if N > 1:
        for n in range(2, (N//2)+1):
            if N % n == 0:
                return False
        return True
    else:
        return 'Enter numbers greater than 1'
    

# print(5//2)
# print(27//10)
# print(99//10)
# print(-33//10)

print(is_prime(4))
print(is_prime(51))

print(is_prime(1001))
print(is_prime(1))
print(is_prime(51))

print(is_prime(1009))
print(is_prime(1297))
print(is_prime(1000081))
# print(type(5) == 'int')