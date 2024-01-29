
from turtle import Turtle
import random

# DONE make one random car
# DONE assign car a random colour
# DONE have said car move from right to left
# DONE make the car travel a litte smoother.
# DONE have car spawn off the screen to the right(xcor())
# DONE have said car spawn at random Y coordinates.
# DONE create mulitple cars
# DONE ensure that all cars have a random colour
# DONE figure out incident detection.. This may need to be done with one car

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10  # SPEEDING CARS UP OVER TIME


class CarManager(Turtle):
    """Creates and moves car obsticles"""

    def __init__(self):
        """initialising CarManager attributes."""
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        # 1 in 5 chance car will be generated
        random_chance = random.randint(1, 5)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.speed("normal")
            new_car.hideturtle()
            new_car.shapesize(stretch_wid=.8, stretch_len=2)
            new_car.penup()
            Y = random.randint(-220, +220)
            new_car.color(random.choice(COLORS))
            new_car.goto(+310, Y)
            new_car.showturtle()
            self.cars.append(new_car)

    def movement(self):
        """allows car to trave along the x coordinates."""
        for car in self.cars:
            car.backward(self.car_speed)

    def increase_difficulty(self):
        """Speeds car up every level reached"""
        self.car_speed += MOVE_INCREMENT


# ================= WORKING BACKUP CODE =========================
"""This code has one moving car. left to right, in random colour and random Y"""


# class CarManager(Turtle):
#     """Creates and moves car obsticles"""

#     def __init__(self):
#         """initialising CarManager attributes."""
#         super().__init__()
#         self.cars = []
#         self.additional_cars()
#         self.movement()

#     def additional_cars(self):
#         self.penup()
#         self.hideturtle()
#         self.shape("square")
#         self.goto(X, Y)
#         self.setheading(180)
#         self.color(random.choice(COLORS))
#         self.shapesize(stretch_wid=.8, stretch_len=2.2)
#         self.showturtle()

#     def movement(self):
#         """allows car to trave along the x coordinates."""
#         self.speed("normal")
#         self.forward(STARTING_MOVE_DISTANCE)
