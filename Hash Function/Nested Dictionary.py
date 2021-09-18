# Nested Dictionary

emp_detail = {'Employee': {'Dave': {'ID': '001', 'Salary': '$2000', 'Designation': 'Team Lead'},
                           'Ava': {'ID': '021', 'Salary': '$1500', 'Designation': 'Associate'}}}
print(emp_detail.keys())
for x in emp_detail.values():
    print(x)
