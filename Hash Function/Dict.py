# Hash function generate key values which then stored in hash table
# Dictionary can be created in two ways 1 is through curly braces {} and other is through dict() function

# curly braces {}
my_dict = {"Dave": "001", "Ava": "002"}
print(my_dict)
print(type(my_dict))

# dict() function
new_dict = dict(Dave='001', Ava='002')
print(new_dict)
print(type(new_dict))

# Updating Values
my_dict['Ava'] = '021'
new_dict['Chris'] = '003'
print(my_dict)
print(new_dict)
my_dict.__delitem__('Dave')
print(my_dict)
