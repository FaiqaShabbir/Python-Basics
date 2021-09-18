import seaborn as sns
import matplotlib.pyplot as plt

graph = sns.load_dataset('tips')
# boxen, violin
sns.catplot(x='day', y='total_bill', data=graph, kind='boxen')
plt.show()
