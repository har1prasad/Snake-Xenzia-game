from turtle import Turtle

SNAKE_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

MOVE_POSITIONS = 20
RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270
       
class Snake:
    """Class for implementing the movement of the snake"""
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        """Create the initial snake segments"""
        for position in SNAKE_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Adding the segments to the snake"""
        snake = Turtle("square")
        snake.color("green")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)

    def extend(self):
        """Extending the segments to the snake"""
        self.add_segment(self.segments[-1].position())

    def right(self):
        """Change the direction of the snake to right"""
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def up(self):
        """Change the direction of the snake to upward"""
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def left(self):
        """Change the direction of the snake to left"""
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def down(self):
        """Change the direction of the snake to downward"""
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def move(self):
        """Moving the snake"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_POSITIONS)