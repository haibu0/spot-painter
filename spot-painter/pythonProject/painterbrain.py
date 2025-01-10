from turtle import Turtle, Screen
import random
import colorgram
from PIL.ImageOps import colorize


# 10 X 10
# SPOT GAP: 50
# SPOT SIZE: 20

class Painter:
    def __init__(self):

        self.color_list = []
        self.make_color_list()

        #self.color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51), (6, 68, 42), (176, 176, 233), (239, 168, 161), (249, 8, 48), (5, 246, 222), (15, 76, 110), (243, 15, 14), (38, 43, 221)]

        self.color_index = 0
        self.painter = Turtle()
        self.painter.hideturtle()
        self.screen = Screen()
        self.screen.colormode(255)
        self.x, self.y = self.screen.screensize()
        self.x = -(self.x) + 150
        self.y = self.y - 50
        self.painter.teleport(self.x, self.y)


    def paint(self):
        self.painter.speed(0) #set to fastest speed
        self.painter.penup()
        self.num_columns = 10

        #DRAW A ROW FOR EACH COLUMN
        for row in range(self.num_columns):
            self.draw_row()
            self.y -= 50
            self.painter.teleport(self.x, self.y)
        self.screen.exitonclick()
    #DRAW A ROW
    def draw_row(self):
        row_size = 10
        for dot in range(row_size):
            self.painter.dot(20, self.choose_random_color())
            self.painter.forward(50)


    #GET THE NEXT COLOR
    def next_color(self):
        # Get the current color and increment the index
        color = self.color_list[self.color_index]
        self.color_index = (self.color_index + 1) % len(self.color_list)  # Cycle to the next color
        return color

    def make_color_list(self):
        colors = colorgram.extract('image.jpg', 25)
        for coloring in colors:
            r = coloring.rgb.r
            g = coloring.rgb.g
            b = coloring.rgb.b
            if not (r > 200 and g > 200 and b > 200):
                new_color = (r, g, b)
                self.color_list.append(new_color)

    def choose_random_color(self):
        next_color = random.choice(self.color_list)
        return next_color