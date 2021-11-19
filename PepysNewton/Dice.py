import random


# simulate one trial of the pepys newton problem, with specified
# no. of rounds, and no. of possible sides on a die being used
def simulator(rounds, sides):
    count = 0
    for i in range(rounds):
        for j in range(sides):
            roll = random.randint(1,6)
            # print stmt for sake of demonstration
            #print(roll)
            if roll == 1:
                count += 1
    # also for nice output
    #print("END TRIAL. COUNT=", count)
    if count < rounds:
        return False
    else:
        return True
