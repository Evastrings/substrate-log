"""Convert hexadecimal to decimal"""

def hexadecimal_to_decimal(string):
    """
    Take a hexadecimal representation of a number and return the decimal representation
    """
    

    string = string.lower()
    result = 0

    hex_dict = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'a': 10,
        'b': 11,
        'c': 12,
        'd': 13,
        'e': 14,
        'f': 15
    }

    for index, digit in enumerate(string):
        if digit not in hex_dict:
            return 'Invalid Hexadecimal Number'
        
        exponent = len(string) - index - 1
        result += hex_dict[digit] * (16 ** exponent)

    return result

hex_c = '7CF'
dec_c = hexadecimal_to_decimal(hex_c)
print(f"{hex_c} to decimal is {dec_c}")

print(hexadecimal_to_decimal('ABCDEF'))