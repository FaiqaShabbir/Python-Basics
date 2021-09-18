import matplotlib.pyplot as plt
import seaborn as sns

sns.set(color_codes=True)
tips = sns.load_dataset("tips")
g = sns.lmplot(x="total_bill", y="tip", hue="smoker", data=tips)
plt.show()
