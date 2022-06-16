
import numpy as np

## Задание 1
a = np.array([1,2,3,3,1,6,8,11,10,7])
a = a.reshape(2,5).T
mean_a = np.mean(a,0)
print (mean_a)

## Задание 2
a_centered = a - mean_a
print (a_centered)

## Задание 3
a_centered_sp = np.dot(a_centered[:,0],a_centered[:,1])
n = a_centered_sp / (a.shape[0]-1)
print (n)

## Задание 4
m =  np.cov(a.T)
print(n == m[0,1])

