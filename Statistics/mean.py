import numpy as np
import scipy.stats
from scipy.stats import mode
my_list = [2, 4, 5, 6, 7, 8, 9, 20, 23, 45, 77, 12, 10, 43, 23, 98, 90]
# 2 4 5 6 7 8 9 10 12 20 23 23 43 45 77 90 98 100
"""
def mean(my_data):
    # 1.0 multiplied with length of data so the floating values will not lost
    return sum(my_data) / (len(my_data) * 1.0)
"""
# print(np.median(my_list))
print("Mean of array:")
my_list.append(100)
np_my_list = np.asarray(my_list)
# use the built in function mean
print(np.mean(np_my_list))
# mean effected by the extreme points
print("Median from the list")
print(np.median(np_my_list))
print(scipy.stats.mode(my_list))

