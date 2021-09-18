import pandas as pd

df1 = pd.DataFrame({"Int_Rate":
    [2, 1, 2, 3], "IND_GDP": [50, 45, 45, 20]},
                    index=[2001, 2002, 2003, 2004])

df2 = pd.DataFrame({"Lower_tier_HPI": [80, 90, 70, 40], "Unemployment":
    [2, 1, 2, 3]}, index=[2001, 2004, 2005, 2008])

"""
result = pd.merge(df1, df2, on="IND_GDP")
print(result)
"""
# Common
"""
joined = df1.join(df2)
print(joined)"""
# For concatenation column headers should be the same
concat = pd.concat(df1, df2)
print(concat)
