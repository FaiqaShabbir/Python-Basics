import pandas as pd

emp_detail = {'Employee': {'Dave': {'ID': '001', 'Salary': '$2000', 'Designation': 'Team Lead'},
                           'Ava': {'ID': '021', 'Salary': '$1500', 'Designation': 'Associate'}}}
df = pd.DataFrame(emp_detail['Employee'])
print(df)

