"""Monte Carlo simulation of getting heads or tail"""

import random


def sim_probablity(num_heads, num_flips):
    """
    Monte Carlo simulation to compute the probability of getting a given number of heads in a given number of flips of a fair coin.
    """
    if not all(isinstance(num, int) for num in (num_heads, num_flips)):
        return 'arguments must be an int'

    
    success = 0

    for i in range(0, 1000):
        count_heads = 0
        for flip in range(0, num_flips):
            random_num = random.random()
            if random_num < 0.5:
            # random_num < 0.5 is head, otherwise is tail
                count_heads += 1
        if count_heads == num_heads:
            success += 1
                

    return success / 1000



# for i in range(0, 5):
#     print(sim_probablity(500, 1000))
# for i in range(1, 10):
#     print(random.random())

# print(sim_probablity(3, 5))