#BMI.py
try:
    weight,height = eval(input("Input your weight(kg), height(m):"))
    bmi = weight / height *2
    if bmi >= 30:
        print("Too fat")
    elif bmi >= 25:
        print("A little fat")
    elif bmi >= 18.5:
        print("Normal")
    elif bmi > 0:
        print("Too thin")
    else:
        print("Pls input the correct number")
except:
    print("The input is wrong")
finally:
    print("Please keep healthy")
