"""Return Fibonacci sequence of n terms"""

def fibonacci(n):
    """
    Starting with 0,1, generate each term by adding the previous two terms.
    """
    if not isinstance(n, int):
        return 'Invalid Integer'

    if n < 1:
        return []

    terms = [0, 1]
    if n == 1:
        return [0]

    while len(terms) < n:
        last_two_terms = terms[-2]
        previous_term = terms[-1]
        next_term = last_two_terms + previous_term
        terms.append(next_term)

    return terms


def fibonacci_nth(n):
    """
    Returns nth term of the fibonacci sequence
    """
    if not isinstance(n, int):
        return 'Invalid Integer'
    
    if n < 1:
        return 'n must be at least 1'

    if n == 1:
        return 0
    if n == 2:
        return 1

    return fibonacci_nth(n - 1) + fibonacci_nth(n - 2)

if __name__ == '__main__':

    print(fibonacci(13))
    for i in range(-4, 13):
        print(fibonacci(i))

    test = [1, -2, 3, 7, 8, 13, 0, 1, 2, 3, 4, 5, 6, 7, 8, 'r,', '20', -56, '13']
    print("=== Testing the nth term function ===")
    for i in test:
        print(f"{i}th term in the fibonacci sequence is {fibonacci_nth(i)}")