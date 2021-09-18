import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]

sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]

plt.plot([], [], label='Sleeping', color='m', linewidth=5)
plt.plot([], [], label='Eating', color='c', linewidth=5)
plt.plot([], [], label='Working', color='r', linewidth=5)
plt.plot([], [], label='Playing', color='k', linewidth=5)

plt.stackplot(days, sleeping, eating, working, playing, colors=['m', 'c', 'r', 'k'])


plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Stack Plot')

plt.legend()
plt.show()