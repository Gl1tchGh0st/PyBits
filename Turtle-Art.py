from turtle import fd, rt
import turtle

def spiral(n, d):
    for i in range(1, n + 1):
        fd(i * 2)
        rt(d)

def ifboi():
    if choice == "classic" or choice == "Classic" or choice == "1":
        spiral(100, 91)
    elif choice == "reverse" or choice == "Reverse" or choice == "2":
        spiral(100, 89)
    elif choice == "maze" or choice == "Maze" or choice == "3":
        spiral(100, 90)
    elif choice == "flower" or choice == "Flower" or choice == "4":
        spiral(100, 100)


print("""\
(1) Classic
(2) Reverse
(3) Maze
(4) Flower
""")

choice = input("Enter your choice here: ")
ifboi()
