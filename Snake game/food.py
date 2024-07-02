from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__() # inheriting from turtle class
        self.food = None
        self.create_food()

    def create_food(self):
        """Create the food object and place it at a random position."""
        self.shape("circle")
        self.resizemode("user")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.speed("fastest")
        self.penup()
        self.refresh_position()

    def refresh_position(self):
        """Randomly reposition the food on the screen."""
        x_cor = random.randint(-275, 275)
        y_cor = random.randint(-275, 260)
        self.goto(x_cor, y_cor)