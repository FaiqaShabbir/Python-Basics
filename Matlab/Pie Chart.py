import matplotlib.pyplot as plt

slices = [7, 2, 3, 13]
activities = ['sleeping', 'eating', 'working', 'playing']
cols = ['c', 'm', 'r', 'b']

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=180,
        shadow=True,
        explode=(0.1, 0.1, 0.1, 0.1),
        autopct='%1.1f%%')

plt.title('Pie Chart')
plt.show()
