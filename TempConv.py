#TempConvert.py
val = input("Input the tempreture:")
if val[-1] in ['C','c']:
    f = 1.8 * float(val[0:-1]) + 32
    print("The F is %.2fF"%f)
elif val[-1] in ['F','f']:
    c = (float(val[0:-1]) - 32) / 1.8
    print("The C is %.2fC"%c)
else:
    print("Input Error!")
