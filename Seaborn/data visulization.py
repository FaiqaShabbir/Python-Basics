import scipy.stats
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

graph = np.random.normal(loc=5, size=200, scale=2)
sns.displot(graph)
plt.show()
