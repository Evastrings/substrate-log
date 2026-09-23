"""Sample an index from an arbitrary discrete probability distribution."""

import random

def random_draw(distribution):
    """
    samples a random number such that distribution[i] is the probability of sampling index i .
    """
    if not all(isinstance(num, float) for num in distribution):
        return 'distribution values must be float'
    test_sum = 0
    for probabilty in distribution:
        test_sum += probabilty

    if test_sum != 1:
        return 'Invalid distribution. Distribution total must be equal to 1'

    cumulative_sum = 0
    cumulative_distribution = []

    for index in distribution:
        cumulative_sum += index
        cumulative_distribution.append(cumulative_sum)

    random_num = random.random()
    for i, draw in enumerate(cumulative_distribution):
        if draw >= random_num:
            return i

print(random_draw([0.4, 0.2, 0.2, 0.2]))

test_distribution = [0.4, 0.2, 0.2, 0.2]
count = [0, 0, 0, 0]
for i in range(10000):
    index = random_draw(test_distribution)
    count[index] += 1

print(f" value of distrubution count: {count}")

n_dist = []
for v in count:
    val = v / 10000
    val = round(val, 1)
    n_dist.append(val)

print(f" This is the value of the distribution after test {n_dist}")

print("=====TEST CASE FOR SEVERAL DISTRIBUTIONS====")
tests = [[0.9, 0.1], [0.3, 0.2, 0.7], [0.5, 0.5], [0.2, [0.7], '2'], [0.1, 0.2, 0.3, 0.4]]
for test in tests:
    counter = [0, 0, 0, 0]
    for i in range(10000):
        index = random_draw(test)
        counter[index] += 1
    print(f" the distribution of {test} after the random draw distribution is {counter}")
    distro = []
    for new in counter:
        proba = new / 10000
        proba = round(proba, 1)
        distro.append(proba)
    print(f" the distribution of {test} after the random draw distribution is {counter}, then after division, the probablity from distro is {distro}")