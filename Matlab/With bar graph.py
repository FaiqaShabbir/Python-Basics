from matplotlib import pyplot as plt

plt.bar([1, 3, 5, 2, 7, 9], [6, 4, 8, 9, 1, 9], lable='Example One', color='c')

plt.bar([2, 6, 4, 8, 10], [8, 6, 2, 5, 6], label='Example Two', color='g')

plt.legend()

plt.xlabel("Bar Number")
plt.ylabel("Bar Height")

plt.title("Bar Graph")

plt.show()
