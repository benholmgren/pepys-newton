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


def makeplot (disc, trial):
    data = []
    for i in range(len(trial)):
        if i % disc == 0:
            curfreq = freq(trial[0:i+1])
            data.append(curfreq)
    Plot.plot(data)


if __name__ == '__main__':
    trial1 = experiment(100, 1, 6)
    trial2 = experiment(100, 2, 6)
    trial3 = experiment(100, 3, 6)
    print(freq(trial1))
    print(freq(trial2))
    print(freq(trial3))
    makeplot(5, trial1)
