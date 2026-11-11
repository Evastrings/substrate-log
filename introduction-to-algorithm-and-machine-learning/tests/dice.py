import random

def dice_prob(outcome_check, rolls):

    
    # total_outcomes = []
    counter = 0

    for i in range(rolls):
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)

        outcome_in_1_roll = [dice_1, dice_2]
        # print(outcome_in_1_roll)

        if outcome_in_1_roll == outcome_check:
            counter += 1

    return counter





fig = [6, 6]
prb = dice_prob(fig, 1000)

print(prb)

tests = [10, 100, 1000, 100000, 1000000, 100000000]

for test in tests:
    prob_v = dice_prob(fig, test)
    print(f"The amount of {fig} after {test} rolls is {prob_v}")


# for i in range(0, rolls):
#     dice_1 = random.randint(1, 6)
#     dice_2 = random.randint(1, 6)
#     outcome_in_1_roll = [dice_1, dice_2]
#     print(outcome_in_1_roll)

# # counter = 0
# # for i in range(1, 25):
# a = [6, 6]
# b = [6, 6]
# print(a == b)
