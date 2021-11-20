import numpy as np
import matplotlib.pyplot as plt
random = np.random.default_rng(12345)

#percent of money to bet
x = [.1, .2, .3, .4, .5, .6, .7, .8, .9, 1]

#number of attempts
bets = 1000

final_value = []

for i in x:
    initial = 1
    earnings = 0
    for y in bets:
        attempt = random.random()
        if attempt < i:
            initial = (1+i)*initial
        else:
            initial = (1-i)*initial
    final_value.append(initial)

plt.plot(x, final_value)
        


