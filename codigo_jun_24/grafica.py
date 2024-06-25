import matplotlib.pyplot as plt

from random import randint

x = list(range(10))

y = []
for i in range(10):
    y.append(randint(5, 15))

plt.plot(x, y)
plt.show()
