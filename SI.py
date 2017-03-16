#Seven-segment_Indicator.py
from turtle import *
import time

def paint(pic,a,b,c,d,e,f,g):
    q = pic.clone()
    if a == 1:
        pic.setheading(90)
        pic.fd(100)
        pic.setheading(0)
        pic.pendown()
        pic.fd(50)
        pic.penup()
    if b == 1:
        pic = q.clone()
        pic.fd(50)
        pic.setheading(90)
        pic.fd(50)
        pic.pendown()
        pic.fd(50)
        pic.penup()
    if c == 1:
        pic = q.clone()
        pic.fd(50)
        pic.setheading(90)
        pic.pendown()
        pic.fd(50)
        pic.penup()
    if d == 1:
        pic = q.clone()
        pic.pendown()
        pic.fd(50)
        pic.penup()
    if e == 1:
        pic = q.clone()
        pic.setheading(90)
        pic.pendown()
        pic.fd(50)
        pic.penup()
    if f == 1:
        pic = q.clone()
        pic.setheading(90)
        pic.fd(50)
        pic.pendown()
        pic.fd(50)
        pic.penup()
    if g == 1:
        pic = q.clone()
        pic.setheading(90)
        pic.fd(50)
        pic.setheading(0)
        pic.pendown()
        pic.fd(50)
        pic.penup()

def main():
    #获取当前时间，格式化为YYYYMMDD的字符串
    t = time.strftime('%Y%m%d',time.localtime(time.time()))
    pic = Turtle()
    pic.color("green")
    pic.pensize(5)
    pic.hideturtle()
    pic.speed(10)
    pic.penup()
    i = 1
    for p in t:
        #第一个数字左下角在(-350,-50)，每个字隔50，每画长50
        pic.goto(-400+i*100,-50)
        i = i+1
        #提取每个字符，并绘制
        if p == "0":
            #7段式，需画段置1，横线从上到下为a、g、d，竖线从左到右f、b、e、c
            paint(pic,1,1,1,1,1,1,0)
        elif p == "1":
            paint(pic,0,1,1,0,0,0,0)
        elif p == "2":
            paint(pic,1,1,0,1,1,0,1)
        elif p == "3":
            paint(pic,1,1,1,1,0,0,1)
        elif p == "4":
            paint(pic,0,1,1,0,0,1,1)
        elif p == "5":
            paint(pic,1,0,1,1,0,1,1)
        elif p == "6":
            paint(pic,1,0,1,1,1,1,1)
        elif p == "7":
            paint(pic,1,1,1,0,0,0,0)
        elif p == "8":
            paint(pic,1,1,1,1,1,1,1)
        else:
            paint(pic,1,1,1,1,0,1,1)

main()
