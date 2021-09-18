def lamb(x):
    return lambda y: x + y


t = lamb(5)
print(t(8))
