"""
By Yuanhao WU
"""
def max2(x):
    m1, m2 = (x[1], x[0]) if x[1] > x[0] else (x[0] , x[1])
    for _ in range(2, len(x)):
        if x[_] > m2:
            if x[_] > m1:
                m1 = x[_]
            else:
                m2 = x[_]
    print(f'The max 2 number are {m1} and {m2}.')

if __name__ == '__main__':
    l1 = [2,5,3,1,4]
    max2(l1)
