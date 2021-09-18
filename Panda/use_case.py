import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

country = pd.read_csv("C:\\Users\\faiqa\\OneDrive\\Desktop\\Python\\countries.csv", index_col=0)
df = country.head(10)
df = df.set_index(["Country Code"])
sd = df.reindex(columns=['2011', '2013'])
db = sd.diff(axis=1)
db.plot(kind='bar')
plt.show()
