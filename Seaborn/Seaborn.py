import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

"""sns.set_style("whitegrid")
data = np.random.normal(size=(100, 10)) + np.arange(10) / 2
sns.boxplot(data=data)"""

data = np.random.normal(size=(100, 10)) + np.arange(10) / 2
f, ax = plt.subplots()
sns.violinplot(data=data)
sns.despine(offset=30, trim=True)

plt.show()
