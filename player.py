from turtle import Turtle

STARTING_POSITION = (0, -230)
MOVE_DISTANCE = 10
FINISH_LINE_Y = +240

# DONE Create a turtle player that starts at the bottom of the screen and listen for the "Up"
#    keypress to move the turtle north. If you get stuck, check the video walkthrough in Step 3.
# DONE Register when the turtle makes it to the finish line.
# DONE Reset the turtle back to the start line to start the next level.


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.setheading(90)
        self.penup()
        self.shape("turtle")
        self.color("black", "spring green")
        self.goto(STARTING_POSITION)
        self.showturtle()

    def movement(self):
        """Moves the turtle upwards."""
        self.speed("slowest")
        self.forward(MOVE_DISTANCE)

    def next_level(self):
        """Sends turte back to start of next level"""
        self.goto(STARTING_POSITION)
