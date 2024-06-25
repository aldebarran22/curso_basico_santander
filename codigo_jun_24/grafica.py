import matplotlib.pyplot as plt

from random import randint

x = list(range(10))

y = []
y2 = []
for i in range(10):
    y.append(randint(5, 15))
    y2.append(randint(5, 15))

plt.plot(x, y, color="red", lw=5, ls="-.", label="ES")
plt.plot(x, y2, color="green", lw=5, ls="-.", label="FR")
plt.legend()
plt.show()
