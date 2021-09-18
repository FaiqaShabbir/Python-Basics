# generator with expression

f = range(6)
print("List comp", end=":")
# using list comprehension produce values at once
my_list = [x+3 for x in f]
print(my_list)
print("Generator Expression", end=":")
# Generator Expression
new_list = (x+2 for x in f)
print(new_list)
# but in loop produce values one after other
for x in new_list:
    print(x)

