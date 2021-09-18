import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load an example dataset from the online repository (requires internet).
file = sns.load_dataset("flights")
sns.relplot(x="passengers", y="month", hue='year', data=file)
plt.show()
