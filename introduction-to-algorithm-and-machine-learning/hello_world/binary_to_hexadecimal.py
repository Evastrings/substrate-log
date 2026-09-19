"""Convert binary to hexadecimal."""

from binary_to_decimal import binary_to_decimal
from decimal_to_hexadecimal import decimal_to_hexadecimal

def binary_to_hexadecimal(string):
    """
    Take a binary representation of number and return the hexadecimal representation
    """
    if not isinstance(string, str):
        return 'Enter a string'

    for digit in string:
        if digit not in ('0', '1'):
            return 'Invalid binary number'
    return decimal_to_hexadecimal(binary_to_decimal(string))


tests = ['123', '10', '1', '0', '1101111', '101010', '11010', 'w', 2, '111']
if __name__ == '__main__':
    for test in tests:
        print(f"{test} in hexadecimal is {binary_to_hexadecimal(test)}")

