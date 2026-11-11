"""Script to decode a message where a and b are both integers between 0 and 100"""

from decode_numbers import decode_numbers

encoded_message = [377, 717, 71, 513, 105, 921, 581, 547, 547, 105, 377, 717, 241, 71, 105, 547, 71, 377, 547, 717, 751, 683, 785, 513, 241, 547, 751]


# valid_response = []
# valid_values = []

for a in range(1, 101):
    for b in range(101):
        result_value = decode_numbers(encoded_message, a, b)
        if not result_value:
            continue
        # valid_response.append(result_value)
        print(f"a={a:2}, b={b:3}, result -> '{result_value}'")


# for response in valid_response:
#     print(response)
