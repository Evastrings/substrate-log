""" Triple the last digit then subtracts Four"""

def triple_then_subtract_four(n):
    """
    Starting with 5, generate each term by multiplying the previous term by 3 and subtracting 4.
    """
    if not isinstance(n, int):
        return 'Invalid integer'

    terms = [5]
    
    if n < 1:
        return []

    while (len(terms) < n):

        previous_term = terms[-1]
        next_term = previous_term * 3 - 4
        terms.append(next_term)

    return terms


def triple_then_subtract_four_nth(n):
    """
    Returns the nth term of the 'triple_then_subtract_four' function
    """
    if not isinstance(n, int):
        return 'Invalid integer'

    if n <= 0:
        return 'Enter values greater than 0'

    if n == 1:
        return 5

    return triple_then_subtract_four_nth(n - 1) * 3 - 4

if __name__ == '__main__':
    print(triple_then_subtract_four(8))

    print("=== Testing the nth term function ===")
    for i in range(-1, 8):
        print(f" The {i}th term of this sequence is {triple_then_subtract_four_nth(i)}")

    print(triple_then_subtract_four('2'))
    print(triple_then_subtract_four_nth('w'))