import pandas as pd

# index_col = 0 no index in that particular data1 print
country = pd.read_csv("C:\\Users\\faiqa\\OneDrive\\Desktop\\Python\\annual-enterprise-survey-2020-financial-year-provisional-csv.csv", index_col=0)
country.to_html('edu.html')

