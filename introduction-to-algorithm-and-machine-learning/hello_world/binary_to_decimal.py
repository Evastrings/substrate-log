""" Convert binary numbers to decimal"""

def binary_to_decimal(string):
    """
    Take a binary representation of a number and return the decimal representation.
    """
    index = 1
    result = 0

    for digit in string:
        calc = int(digit) * (2 ** (len(string) - index))
        result += calc
        index += 1

    return result

binn = '11010'

b1 = '1'

b2 = '111'

b3 = '10'

b4 = '11'

b5 = '100'

dinn = binary_to_decimal(binn)
print(f" 11010 in decimal is {dinn}")

print(binary_to_decimal(b1))
test = [b1, b2, b3, b4, b5]
for i in test:
    print(f"The value of {i} in decimal is {binary_to_decimal(i)}")

