# now i'm going to declare map and filter functions within reduce
# function it should be b fun
from functools import reduce

my_list = reduce(lambda x, y: x+y, map(lambda x: x+x, filter(
    lambda x: x > 5, (3, 4, 5, 6, 7, 8, 9)
)))
print(my_list)
