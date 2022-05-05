from random import random
from random import randint
from random import seed
from random import randrange
from random import gauss
from random import choice
from random import shuffle

# Random Floating Point Numbers
seed(7)
print(random(), random())
# if we want to generate random number not lies b/w 0 and 1 then we will:
print(2+10*random())

# Python Random Integers
print(randint(0, 9))

# Integer from random range
print(randrange(-2, 4))

# Random Gaussian Values
print(gauss(0, 7))

# Choosing Randomly From Lists
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 11, 12, 16]
print(choice(list))

#  Shuffling a List Randomly
shuffle(list)
print(list)