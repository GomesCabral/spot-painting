import colorgram
from turtle import Turtle, Screen
import random

# Extract 33 colors from an image.
#colors = colorgram.extract('image.jpg', 33)
#print(colors)

# colorgram.extract returns Color objects, which let you access RGB ...

# my_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     my_colors.append(new_color)

# print(my_colors)
#copy the colors result from my_colors
color_list = [(226, 229, 235), (244, 237, 222), (243, 234, 240), (232, 242, 237), (192, 165, 115), (138, 166, 190), (56, 102, 140), (141, 91, 50), (12, 23, 55), (222, 207, 123), (182, 154, 42), (61, 22, 11), (182, 146, 165), (142, 177, 151), (72, 117, 81), (58, 15, 26), (126, 79, 102), (130, 30, 16), (15, 39, 23), (24, 53, 127), (177, 188, 215), (164, 104, 134), (115, 31, 46), (97, 150, 100), (98, 121, 172), (210, 178, 197), (174, 105, 93), (74, 150, 165), (25, 91, 65), (172, 205, 180), (86, 76, 17), (216, 181, 175), (163, 203, 213)]

heni = Turtle()
heni.speed("fastest")
heni.colormode(255)
heni.penup()
heni.hideturtle()
heni.setheading(225)
heni.forward(300)
heni.setheading(0)
num_of_dots = 100

for num in range(1, num_of_dots + 1):
    heni.dot(10, random.choice(color_list))
    heni.forward(50)

    if num % 10 == 0:
        heni.setheading(90)
        heni.forward(50)
        heni.setheading(180)
        heni.forward(500)
        heni.setheading(0)


my_screen = Screen()
my_screen.exitonclick()