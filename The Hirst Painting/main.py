import turtle
from turtle import Turtle, Screen
import random
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
# print((rgb_colors))

color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
              (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
              (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
              (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19),
              (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

turtle.colormode(255)
obj = Turtle()
obj.penup()
obj.hideturtle()

obj.setheading(225)
obj.forward(300)
obj.setheading(0)
number_of_dots = 100
for dot_count in range(1,number_of_dots+1):
    obj.dot(15,random.choice(color_list))
    obj.forward(50)

    if dot_count % 10 == 0:
        obj.setheading(90)
        obj.forward(50)
        obj.setheading(180)
        obj.forward(500)
        obj.setheading(0)



screen = Screen()
screen.exitonclick()