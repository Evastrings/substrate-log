"""Take half of the previous term if it’s even, or multiply by 3 and add 1 if it’s odd."""

def collatz_sequence_instance(n):
    """
    Starting with 25, generate each term by taking half of the previous term if it’s even, or multiplying by 3 and adding 1 if it’s odd.
    """
    if not isinstance(n, int):
        return 'Invalid Integer'

    if n < 1:
        return []

    terms = [25]
    while len(terms) < n:
        previous_term = terms[-1]

        if previous_term % 2 == 0:
            next_term = previous_term // 2
        else:
            next_term = previous_term * 3 + 1
        terms.append(next_term)

    return terms


def collatz_sequence_instance_nth(n):
    """
    Returns the nth term in the collatz_sequence_function
    """
    if not isinstance(n, int):
        return 'Invalid Integer'

    if n < 1:
        return 'n must be greater than 1'

    if n == 1:
        return 25

    previous_term = collatz_sequence_instance_nth(n - 1)
    if previous_term % 2 == 0:
        return previous_term // 2
    else:
        return previous_term * 3 + 1

if __name__ == '__main__':

    for i in range(-5, 12):
        print(collatz_sequence_instance(i))

    print("===Testing the nth term sequence===")
    for i in range(-2, 25):
        print(f"The {i}th term in this sequence is {collatz_sequence_instance_nth(i)}")