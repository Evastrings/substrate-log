""" Convert binary numbers to decimal"""

def binary_to_decimal(string):
    """
    Take a binary representation of a number and return the decimal representation.
    """

    for digits in string:
        if digits not in ("0", "1"):
            return 'Invalid binary number'
    result = 0

    for index, digit in enumerate(string):
        exponent = len(string) - index - 1
        result += int(digit) * (2 ** exponent)

    return result
