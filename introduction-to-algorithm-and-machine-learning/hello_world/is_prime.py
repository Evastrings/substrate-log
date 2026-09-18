"""Check whether an integer is prime"""

def is_prime(N):
    """
    Checks whether an interger N > 1 is prime by checking whether there exists 
    some n ∈ {2,3,4,...,⌊N/2⌋} such that n divides N.
    """
    if N > 1:
        for n in range(2, (N//2)+1):
            # or (N**2) + 1
            if N % n == 0:
                return False
        return True
    else:
        return False
    