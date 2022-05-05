mylist = []
for i in 'Faiqa':
    mylist.append(i)

print(mylist)

mywish = [i for i in 'Faiqa']
mywish = [i * 2 for i in {1, 3, 5}]
print(mywish)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sd = list(filter(lambda x: x % 3 == 0, numbers))
print(sd)
