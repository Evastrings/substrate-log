"""Converts hexadecimal numbers to binary"""

from hexadecimal_to_decimal import hexadecimal_to_decimal
from decimal_to_binary import decimal_to_binary

def hexadecimal_to_binary(string):
    """
    Take a hexadecimal representation of a number and return the binary representation.
    """
    decimal = hexadecimal_to_decimal(string)

    if decimal == 'Invalid Hexadecimal Number' or decimal == 'Enter a string':
        return decimal
    
    return decimal_to_binary(decimal)

tests = ['abcdef', 'g', 'fc1', '0', 8, '32']

for test in tests:
    print(f"{test} in binary is {hexadecimal_to_binary(test)}")