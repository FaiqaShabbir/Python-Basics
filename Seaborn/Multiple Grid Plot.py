import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""a = sns.load_dataset('iris')
b = sns.FacetGrid(a, col='species')
b.map(plt.hist, 'sepal_length')

gra = sns.load_dataset('iris')
sns.pairplot(gra, hue='species', size=2.5)
plt.show()
"""
sns.set(style="ticks")
graph = sns.load_dataset('flights')
b1 = sns.PairGrid(graph)
b1.map(plt.scatter)
plt.show()
