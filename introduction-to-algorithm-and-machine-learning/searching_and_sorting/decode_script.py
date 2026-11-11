"""Script to decode a message where a and b are both integers between 0 and 100"""

from decode_numbers import decode_numbers

encoded_message = [377, 717, 71, 513, 105, 921, 581, 547, 547, 105, 377, 717, 241, 71, 105, 547, 71, 377, 547, 717, 751, 683, 785, 513, 241, 547, 751]

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

a = 100
b = 100

valid_response = []

for i in range(a + 1):
    for j in range(b + 1):
        result_value = decode_numbers(encoded_message, i, j)
        if result_value == False or result_value == 'a cannot be 0':
            continue
        valid_response.append(result_value)

for response in valid_response:
    print(response)
