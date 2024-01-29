from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("black")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.setposition(-200, +200)
        self.write(f"LEVEL: {self.level}", move=False, align="center",
                   font=FONT)

    def increment_score(Self):
        Self.clear()  # Clear will refresh the screen so that 1 doesn't go ontop of 0
        Self.level += 1
        Self.update_scoreboard()

    def game_over(self):
        self.hideturtle()
        self.penup()
        self.setposition(0, 0)
        self.color("black")
        self.write("GAME OVER", move=False, align="center", font=FONT)
