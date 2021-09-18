import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use("fivethirtyeight")
df = pd.DataFrame({"Day": [1, 2, 3, 4], "Visitors":
                   [200, 100, 230, 300],
                   "Bonus_Rate": [20, 45, 60, 10]})
# set index which column header you wand
df.set_index("Day", inplace=True)
df.plot()
plt.show()
