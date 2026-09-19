"""Convert hexadecimal to decimal"""

def hexadecimal_to_decimal(string):
    """
    Take a hexadecimal representation of a number and return the decimal representation
    """

    string = string.lower()
    result = 0
    hex_dict = {
        'a': 10,
        'b': 11,
        'c': 12,
        'd': 13,
        'e': 14,
        'f': 15
    }

    for index, digit in enumerate(string):
        exponent = len(string) - index - 1

        if digit not in hex_dict:
            result += int(digit) * (16 ** exponent)

        else:
            result += hex_dict[digit] * (16 ** exponent)

    return result

hex_c = '7CF'
dec_c = hexadecimal_to_decimal(hex_c)
print(f"{hex_c} to decimal is {dec_c}")