import seaborn as sns
import matplotlib.pyplot as plt

graph = sns.load_dataset('titanic')
sns.relplot(x='sex', y='survived', data=graph, kind='line')
plt.show()
