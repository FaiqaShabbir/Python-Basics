# minimum
f = range(6)
print("Generator Expression", end=":")
loop = (x+2 for x in f)
print(loop)
print(min(loop))
