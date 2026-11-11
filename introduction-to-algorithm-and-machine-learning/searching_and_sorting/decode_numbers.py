"""Write a function that attempts to decode number arrays under the assumption that the encoding function was ax + b"""
ALPHABET_CODE = {
    0: ' ',
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
    6: 'f',
    7: 'g',
    8: 'h',
    9: 'i',
    10: 'j',
    11: 'k',
    12: 'l',
    13: 'm',
    14: 'n',
    15: 'o',
    16: 'p',
    17: 'q',
    18: 'r',
    19: 's',
    20: 't',
    21: 'u',
    22: 'v',
    23: 'w',
    24: 'x',
    25: 'y',
    26: 'z'
}


def decode_numbers(numbers, a, b):
    """
    decode number arrays assuming the encoding function was ax + b
    returns the message if true, otherwise returns false
    """

    if not all(isinstance(number, int) for number in numbers):
        return 'Invalid Integer'
    if not all(isinstance(v, int) for v in [a, b]):
        return 'Invalid Integer'
    
    if a == 0:
        return 'a cannot be 0'

    result = ''
    for num in numbers:
        new_number_code = (num - b) / a
        if new_number_code not in ALPHABET_CODE:
            return False
        letter = ALPHABET_CODE[new_number_code]
        result += letter

    return result
        

# n = [3, 1, 9, 31, 15]
# wrd = decode_numbers(n, 2, 1)
# print(wrd)

# d = [5, 18, 1, 14, 4, 5, 0, 4, 1, 20, 5, 0, 1, 0, 12, 9, 22, 5]
# tt = decode_numbers(d, 0, 0)
# print(tt)

# sw = [21, 14, 13, 5, 9, 0, 4, 1, 20, 20, 5, 0, 1, 11, 9, 18, 1, 13, 5, 26, 21, 0, 14, 9, 0, 11, 1, 5, 20, 5, 0, 13, 9, 19, 5, 18, 21]
# tsw = decode_numbers(sw, 1, 0)
# print(tsw)

# sw2 = [20, 17, 19, 6, 2, 5, 1, 24, 10, 15, 8, 20]
# tsw2 = decode_numbers(sw2, 1, 1)
# print(tsw2)

# tests = [[[3, 1, 9, 31, 15], 1, 0], [[5, 18, 1, 14, 4, 5, 0, 4, 1, 20, 5, 0, 1, 0, 12, 9, 22, 5], 1, 0], [[20, 17, 19, 6, 2, 5, 1, 24, 10, 15, 8, 20], 1, 1], [[3, 1, 9, 31, 15], 1, 1], [[3, 1, 9, 31, 15], 2, 2], [[3, 1, 9, 31, 15], 1, 2]]

# for test in tests:
#     decoded = decode_numbers(test[0], test[1], test[2])
#     print(f"The decoded array'{test[0]}' is '{decoded}'")