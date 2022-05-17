import numpy as np
#### Joining
# arr1 = np.array([1, 2, 3])
#
# arr2 = np.array([4, 5, 6])
#
# arr = np.concatenate((arr1, arr2))
#
# print(arr)

# arr1 = np.array([[1, 2], [3, 4]])
#
# arr2 = np.array([[5, 6], [7, 8]])
#
# arr = np.concatenate((arr1, arr2), axis=1)
#
# arr = np.concatenate((arr1, arr2), axis=0)
# print(arr)
#
# ###### Spliting
#
# arr = np.array([1, 2, 3, 4, 5, 6])
#
# newarr = np.array_split(arr, 3)
#
# print(newarr)

##### Search

# arr = np.array([1, 2, 3, 4, 5, 4, 4])
#
# x = np.where(arr == 4)
#
# print(x)

###### Sorting

# arr = np.array(['banana', 'cherry', 'apple'])
#
# print(np.sort(arr))
#
# arr = np.array([3, 2, 0, 1])
#
# print(np.sort(arr))

######   Filtering
import numpy as np

arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)

###### Filtering2

arr = np.array([41, 42, 43, 44])


filter_arr = []


# for element in arr:
#   if element > 42:
#     filter_arr.append(True)
#   else:
#     filter_arr.append(False)
#
# newarr = arr[filter_arr]
#
# print(filter_arr)
# print(newarr)

#################################################    Datetime module  ########################################################

import datetime

x = datetime.datetime.now()
print(x)

print(x.year)
print(x.strftime("%A"))

x = datetime.datetime(2020, 5, 17) #create

print(x)


x = datetime.datetime(2018, 6, 1)  #format

print(x.strftime("%B"))