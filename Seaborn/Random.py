import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

plt.style.use('classic')

x = pd.DataFrame({'Day': [1, 2, 3, 4, 5, 6, 7], 'Grocery': [30, 80, 45, 23, 51, 46, 76], 'Clothes': [13, 40, 34, 23, 54, 67, 98], 'Utensils': [12, 32, 27, 89, 54, 10, 7]})
y = pd.DataFrame({'Day': [8, 9, 10, 11, 12, 13, 14], 'Grocery': [30, 80, 45, 23, 51, 46, 76], 'Clothes': [13, 40, 34, 23, 54, 67, 98], 'Utensils': [12, 32, 27, 89, 54, 10, 7]})
mean, cov = [0, 1], [(1, .5), (.5, 1)]
data = np.random.multivariate_normal(mean, cov, 200)
with sns.axes_style("white"):
    sns.jointplot(x=x, y=y, kind='kde', color='b')
plt.show()

# data1 = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=2000)
# data1 = pd.DataFrame(data1, columns=['x', 'y'])
# with sns.axes_style('white'):
#    sns.jointplot("x", "y", data1, kind='kde', color='b')

# plt.show()


