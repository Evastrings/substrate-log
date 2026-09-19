"""Convert decimal to hexadecimal"""

def decimal_to_hexadecimal(string):
    """
    Take a decimal representation of a number and return the hexadecimal representation
    """
    reversed_hex_dict = {
        '0': '0',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        '10': 'a',
        '11': 'b',
        '12': 'c',
        '13': 'd',
        '14': 'e',
        '15': 'f'
    }

    if not isinstance(string, str):
        return 'Enter a String'
    
    for digit in string:
        if digit not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            return 'Invalid decimal number'

    if string == '0':
        return reversed_hex_dict[string]

    string = int(string)
    result = ''
    while string != 0:
        result = reversed_hex_dict[str(string % 16)] + result
        string //= 16

    return result
