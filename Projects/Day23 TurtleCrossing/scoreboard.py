from turtle import Turtle
ALIGNMENT = "left"
FONT = ("Courier", 20, "normal")
SCOREBOARD_POS = (-270, 250)


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(SCOREBOARD_POS)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def next_level(self):
        self.level += 1
        self.update_scoreboard()

    def reset_score(self):
        self.level = 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
