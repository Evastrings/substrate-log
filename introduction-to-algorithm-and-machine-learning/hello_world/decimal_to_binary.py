"""Convert decimal to binary"""

def decimal_to_binary(string):
    """
    Take a decimal representation of a number and return the binary representation.
    """

    if not isinstance(string, str):
        return 'Invalid decimal string'
    
    for digit in string:
        if digit not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            return 'Invalid decimal number'

    string = int(string)
    binary_num = ''
    result = ''

    if string == 0:
        return str(string)
    
    while string != 0:
        binary_num += str(string % 2)
        string //= 2

    for i in range(1, len(binary_num) + 1):
        result += binary_num[-i]

    return result


test = [0, 1, 2, 3, 4, 5, 8, 16, 26, 32, '64', 'a3', 56]
tests = [2]

for nu in test:
    print(f"{nu} converted to binary number is {decimal_to_binary(nu)}")