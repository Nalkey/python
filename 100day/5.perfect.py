"""
By Yuanhao WU
"""
import math

for i in range(1,10000):
    sum = 1
#    print('i is %d' % i)
    for j in range(2,int(math.sqrt(i))+1):
        if i % j==0:
            sum += j + i/j
#    print('sum is %d' % sum)
    if sum == i:
        print(i, end=' ')
