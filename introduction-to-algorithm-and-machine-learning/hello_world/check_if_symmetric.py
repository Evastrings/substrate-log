# a function that checks if a string is symettric

def check_if_symmetric(string):
    """
    returns True if the input string is symmetric,
    returns False if not
    """

    #ignoring capitalization
    string = string.lower()
    reversed_string = ""
    for i in range(1, len(string) + 1):
        reversed_string += string[-i]

    return string == reversed_string

# print(check_if_symmetric("Civic"))

# print("==second==")
# print(check_if_symmetric('!ab123 4 321ba!'))
# print(check_if_symmetric("batman"))
# print(check_if_symmetric("racecar"))
# print(check_if_symmetric(''))

