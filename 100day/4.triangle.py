"""
By Howard WU
"""

row = int(input('row:'))
for i in range(row):
    for _ in range(row-i-1):
        print(' ', end='')
    for _ in range(i+1):
        print('*', end='')
    print()
