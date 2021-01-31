"""
By Yuanhao WU
"""

res = 0
num = int(input('num = '))

while num>0:
    res = res*10 + num%10
    num //= 10
print(res)
