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

print(fibonacci(13))
for i in range(-4, 13):
    print(fibonacci(i))

    