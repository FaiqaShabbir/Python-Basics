from matplotlib import pyplot as plt

plt.bar([0.25, 1.25, 2.25, 3.25, 4.25], [50, 40, 70, 80, 20],  width=.5)
plt.bar([0.75, 1.75, 2.75, 3.75, 4.75], [80, 20, 20, 50, 60],  width=.5, color='r')
plt.legend()
plt.xlabel('Days')
plt.ylabel('Distance (kms)')
plt.title('Information')
plt.show()

# Arrow
fig = plt.figure()
ax = fig.add_subplot(111)
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
plt.axis([-5, 5, -5, 5])
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.grid()
plt.arrow(0, 0, 3, 1, head_width=0.2, color='r', length_includes_head=True, label='u')
plt.arrow(0, 0, 1, 3, head_width=0.2, color='r', length_includes_head=True, lable='v')
plt.arrow(0, 0, 4, 4, head_width=0.2, color='r', length_includes_head=True, label='u+v')
ax.legend()
plt.show()
# pie chart
days = [1, 2, 3, 4, 5]

sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]
slices = [7, 2, 2, 13]
activities = ['sleeping', 'eating', 'working', 'playing']
cols = ['c', 'm', 'r', 'b']

plt.pie(slices,

        labels=activities,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0, 0.1, 0, 0),
        autopct='%1.1f%%')

plt.title('Pie Plot')
plt.show()
