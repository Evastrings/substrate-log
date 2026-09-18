"""Count the number of each character in a string"""

def count_characters(string):
    """
    Counts the number of each character in a string and returns the count in a dictionary.
    """

    string = str(string)
    string = string.lower()
    result = {}

    for element in string:
        if element not in result:
            counter = 0
            for char in string:
                if element == char:
                    counter += 1

            result.update({element: counter})

    return result

test = count_characters('A cat!!!')
print(test)

