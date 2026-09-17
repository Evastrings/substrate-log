"""This function turns a list of numbers to string"""

def convert_to_letters(string):
    """
    This is the inverse of convert_to_numbers. For example: [1,0,3,1,20] becomes 'a cat'
    """
    alphabet = " abcdefghijklmnopqrstuvwxyz"
    new_letters = ""

    for num in string:
        for index, letter in enumerate(alphabet):
            if num == index:
                new_letters += letter

    return new_letters

print(convert_to_letters([1,0,3,1,20]))
print(convert_to_letters([20, 8, 9, 19, 0, 9, 19, 0, 20, 8, 5, 0, 3, 8, 15, 9, 3, 5, 0, 15, 6, 0, 19, 20, 5, 9, 14, 19, 0, 7, 1, 20, 5]))