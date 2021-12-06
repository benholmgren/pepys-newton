import Plot
import Dice


# run simulator for desired no. trials
def experiment(trials, rounds, sides):
    outcomes = []
    for i in range(trials):
        outcomes.append(Dice.simulator(rounds, sides))
    return outcomes


# compute frequency of successes, given list of boolean outcomes
def freq(outcomes):
    count = 0
    for outcome in outcomes:
        if outcome:
            count += 1
    return count / len(outcomes)


def makeplot (disc, trial, trialnum):
    data = []
    indices = []
    for i in range(len(trial)):
        if i % disc == 0:
            curfreq = freq(trial[0:i+1])
            data.append(curfreq)
            indices.append(i)
    Plot.plot(data, trialnum, indices)


if __name__ == '__main__':
    # test out each scenario 1000 times
    trial1 = experiment(1000, 1, 6)
    trial2 = experiment(1000, 2, 6)
    trial3 = experiment(1000, 3, 6)
    print("Results Over 1000 Trials:")
    print("Scenario 1 Success Frequency:", freq(trial1))
    print("Scenario 2 Success Frequency:", freq(trial2))
    print("Scenario 3 Success Frequency:", freq(trial3))
    print()

    # these sections take longer to run, so they're commented

    #trial11 = experiment(100000, 1, 6)
    #trial22 = experiment(100000, 2, 6)
    #trial33 = experiment(100000, 3, 6)
    #print("Results Over 100000 Trials:")
    #print("Scenario 1 Success Frequency:", freq(trial11))
    #print("Scenario 2 Success Frequency:", freq(trial22))
    #print("Scenario 3 Success Frequency:", freq(trial33))
    #print()

    #trial111 = experiment(1000000, 1, 6)
    #trial222 = experiment(1000000, 2, 6)
    #trial333 = experiment(1000000, 3, 6)
    #print("Results Over 1000000 Trials:")
    #print("Scenario 1 Success Frequency:", freq(trial111))
    #print("Scenario 2 Success Frequency:", freq(trial222))
    #print("Scenario 3 Success Frequency:", freq(trial333))
    #print()


    #makeplot(50, trial1, "Scenario 1 Over 1000 Trials")
    #makeplot(50, trial2, "Scenario 2 Over 1000 Trials")
    #makeplot(50, trial3, "Scenario 3 Over 1000 Trials")
