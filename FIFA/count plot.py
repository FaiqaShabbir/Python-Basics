import matplotlib
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\faiqa\\OneDrive\\Desktop\\Python\\FullData.csv")
plt.figure(figsize=(15, 32))
sns.countplot(y=df.Nationality, palette="Set2")
plt.show()
