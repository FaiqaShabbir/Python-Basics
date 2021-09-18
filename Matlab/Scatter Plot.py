import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7]
y = [5, 2, 4, 7, 8, 2, 9]

plt.scatter(x, y, label='skitscat', color='c')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot')
plt.legend()
plt.show()
