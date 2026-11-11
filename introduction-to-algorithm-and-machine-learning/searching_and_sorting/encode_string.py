""" Write a function that encode strings using linear encoding function f(x) = ax + b"""

ALPHABET = {
    ' ': 0,
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26
}

def encode_string(string, a, b):
    """
    encode strings using linear encoding function and returns the resulting arrays of numbers
    """
    if not isinstance(string, str):
        return 'Invalid String'
    if not all(isinstance(v, int) for v in [a, b]):
        return 'Invalid Integer'

    string = string.lower()
    result = []

    for letter in string:
        if letter not in ALPHABET:
            return 'Invalid Character'
        new_letter_code = ALPHABET[letter] * a + b
        result.append(new_letter_code)

    return result

# test_string = 'a dog'

# test_string2 = 'unmei datte akiramezu ni kaete miseru'

# tests = ['a dog', 'erande date a live', 'unmei datte akiramezu ni kaete miseru', 'its just so peak']

# # print(encode_string(test_string, 1, 0))

# for test in tests:
#     encode = encode_string(test, 1, 0)
#     print(f" encoded string '{test}' is {encode}")

# tests_v2 = [['a cat', 'x', 0], ['spread wings', 1, 1], [' abcdefg', 1, 0], [5, '4', 4]]

# for test in tests_v2:
#     encode = encode_string(test[0], test[1], test[2])
#     print(f" encoded string '{test[0]}' is {encode}")