from turtle import *


def main():
    setup(1000, 800, 0, 0)
    pensize(10)
    seth(0)
    for i in range(3):
        fd(200)
        seth(i*120+120)

main()
