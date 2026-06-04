# numpy_investigation.py
import numpy as np

arr = np.array([1, 2, 3])
lst = [1, 2, 3]

print (arr)
#lst.
#arr.
m1 = np.random.randint(1, 10, (4, 4))
print (m1)

m2 = np.random.randint(1, 10, (4, 4))
print (m2)

print (m1 + m2)

print (m1)
print (m1 * 10)

print (m1.reshape((2, 8)))
# print (m1.reshape((3, 8)))

arr = np.array(range(1, 17)).reshape((4, 4))

print (arr)

print(arr[2][2])
print(arr[1:3]) # rows 2 & 3
print(arr[1:3,1:3])
print(arr[:, 1:2])

