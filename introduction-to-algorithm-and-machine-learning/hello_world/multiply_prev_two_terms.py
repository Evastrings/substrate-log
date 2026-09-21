"""Return n sequence of the product of previous two terms"""

def multiply_prev_two_terms(n):
    """
    Starting with 2, -3, generate each term by mulitplying the previous two terms.
    """
    if not isinstance(n, int):
        return 'Invalid Integer'

    if n < 1:
        return []

    terms = [2, -3]
    if n == 1:
        return [2]

    while len(terms) < n:
        next_term = terms[-2] * terms[-1]
        terms.append(next_term)

    return terms


def multiply_prev_two_terms_nth(n):
    """
    Returns nth term of the multiply_prev_two_terms sequence
    """
    if not isinstance(n, int):
        return 'Invalid Integer'
    
    if n < 1:
        return 'n must be at least 1'

    if n == 1:
        return 2
    if n == 2:
        return -3

    return multiply_prev_two_terms_nth(n - 1) * multiply_prev_two_terms_nth(n - 2)

if __name__ == '__main__':

    print(multiply_prev_two_terms(13))
    for i in range(-4, 14):
        print(multiply_prev_two_terms(i))

    test = [1, -2, 3, 7, 8, 13, 0, 1, 2, 3, 4, 5, 6, 7, 8, 'r', '20', -56, '13']
    print("=== Testing the nth term function ===")
    for i in test:
        print(f"{i}th term in the multiply_prev_two_terms sequence is {multiply_prev_two_terms_nth(i)}")