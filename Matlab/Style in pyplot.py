from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')

x = [5, 8, 10]
y = [10, 8, 16]

x1 = [6, 9, 11]
y1 = [6, 15, 5]

plt.plot(x, y, 'g', label='line one', linewidth=3)
plt.plot(x1, y1, 'b', label='line two', linewidth=3)

plt.title('Epic Info')
plt.xlabel('X axis')
plt.ylabel('Y axis')

plt.legend()

plt.grid(True, color='k')

plt.show()
