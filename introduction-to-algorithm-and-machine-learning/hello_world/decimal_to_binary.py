"""Convert decimal to binary"""

def decimal_to_binary(string):
    """
    Takeadecimal representation of a numberand return the binary representation.
    """

    for digit in str(string):
        if digit not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            return 'Invalid decimal number'

    string = int(string)
    binary_num = ''
    result = ''

    if string == 0:
        return str(string)
    
    while string != 0:
        # print(string)
        binary_num += str(string % 2)
        string //= 2

    # print(binary_num)
    for i in range(1, len(binary_num) + 1):
        result += binary_num[-i]

    return result

test = [0, 1, 2, 3, 4, 5, 8, 16, 26, 32, '64', 'a3', 56]
tests = [2]

for nu in test:
    print(f"{nu} converted to binary number is {decimal_to_binary(nu)}")