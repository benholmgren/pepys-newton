import random


# simulate one trial of the pepys newton problem, with specified
# no. of rounds, and no. of possible sides on a die being used
def simulator(rounds, sides):
    count = 0
    roll_results = []
    for i in range(rounds):
        for j in range(sides):
            roll = random.randint(1,6)
            # for demonstration, list results
            roll_results.append(roll)
            if roll == 1:
                count += 1
    # print for nice output
    #print("Roll Results:", roll_results)
    #print("Total Rolls of '1':", count)
    outcome = False
    if count >= rounds:
        outcome = True
    #print("Success?", outcome)
    #print()

    return outcome