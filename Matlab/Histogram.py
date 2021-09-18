import matplotlib.pyplot as plt

population_ages = [22, 55, 62, 34, 12, 9, 1, 78, 66, 32, 19, 21, 23, 45, 30, 28, 34, 54, 112, 90, 111, 115]

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Histogram')
plt.show()
