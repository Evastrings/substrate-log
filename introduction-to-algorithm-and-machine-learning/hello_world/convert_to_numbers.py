"""Convert strings to numbers."""

def convert_to_numbers(string):
    """
    Returns an array of numbers corresponding to letters in a string.
    where space = 0, a = 1, b = 2 and so on
    """
    alphabet = ' abcdefghijklmnopqrstuvwxyz'
    string = string.lower()
    
    for letter_check in string:
        if letter_check not in alphabet:
            return 'Enter only letters or space'
    index = 0
    numbers_list = []

    while index < len(string):
        for i, letter in enumerate(alphabet):
            if string[index] == letter:
                numbers_list.append(i)
        index += 1

    return numbers_list


word = 'This'

new_list = convert_to_numbers(word)
print(new_list)
print(convert_to_numbers('Hello .'))
print(convert_to_numbers('This is the choice of Steins Gate'))

