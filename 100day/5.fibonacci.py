"""
By Yuanhao WU
"""

pre = 0
cur = 1
count = int(input('count = '))

if count > 1:
    print('1', end=' ')
else:
    print('too small')

for _ in range(count):
    print(pre+cur, end=' ')
    pre,cur = cur,cur+pre
