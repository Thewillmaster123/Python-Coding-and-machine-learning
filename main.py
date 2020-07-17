import numpy as np 

numbers = np.array([[1,2],[3,4]])
print(numbers)
print(numbers.shape)

array2 = np.array([[1,2,3],[4,5,6]])
print(array2)
print(array2[0,2])

num1 = [1,1,1,1,1]
num2 = [1,1,1,1,1]
print(num1 + num2)

for x in range(len(num1)):
  num1[x] = num1[x] + num2[x]
num1.append(3)
print(num1)

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])
print(arr1 + 5)

