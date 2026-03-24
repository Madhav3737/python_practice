import numpy as np

arr = np.array([1,3,4,6,7,8],ndmin=4)
print(arr)
print(arr.ndim)
a = np.array([10,20,30])
b = np.array([10,20,30])
print(a*b)
print(np.append(a,[20]))
print(a)
print(np.insert(a,1,[50]))
print(a)
# a = np.insert(a,1,[50])
# print(a)
c = np.array([[1,2,3],
              [4,5,6]])
print(np.insert(c,1,[7,8],axis=1))
