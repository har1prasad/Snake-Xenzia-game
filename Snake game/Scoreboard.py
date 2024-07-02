from turtle import Turtle

ALING = "center"
FONT = ('Impact', 14, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        """Created the scoreboard and placed it on the upper-center part"""
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270) 
        self.score = 0
        self.showscore()

    def showscore(self):
        """Displaying the score"""
        self.write(f"Score:{self.score}", align=ALING, font=FONT)

    def increase_score(self):
        """increasing the score"""
        self.score += 1
        self.clear()
        self.showscore()

    def gameover(self):
        """displaying game over"""
        self.goto(0,0)
        self.write("Game Over", align=ALING, font=FONT)
