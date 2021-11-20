import matplotlib.pyplot as plt
import numpy as np


def plot(data, title):
       plt.style.use('_mpl-gallery')
       # make data
       np.random.seed(3)
       x = 0.5 + np.arange(len(data))
       y = data

       # plot
       fig, ax = plt.subplots()

       ax.stem(x, y)

       ax.set(xlim=(0, len(data)), xticks=np.arange(0, len(data)),
              ylim=(0, 1), yticks=np.arange(0, 1))
       plt.title(title)
       plt.xlabel("Trial")
       plt.ylabel("Success Frequency")
       plt.show()
