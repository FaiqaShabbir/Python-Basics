import pandas as pd

XYZ_web = {'Day': [1, 2, 3, 4, 5, 6], "visitors": [1000, 2000, 4000, 1000, 3000, 600], 'Bounce_Rate': [20, 20, 23, 15,
                                                                                                       3, 5]}
df = pd.DataFrame(XYZ_web)
print(df)
