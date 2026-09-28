"""This function that check if a string is symettric."""

def check_if_symmetric(string):
    """returns True if the input string is symmetric,
    returns False if not"""

    #ignoring capitalization
    string = string.lower()
    reversed_string = ""
    for i in range(1, len(string) + 1):
        reversed_string += string[-i]

    return string == reversed_string

