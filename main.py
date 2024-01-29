# STEPS - Breaking the project down.
# DONE Move the turtle with key press
# DONE Create and move the cars
# DONE Create multiple cars
# DONE Detect collision with car
# DONE Detect when turtle reaches the other side
# DONE Create a scoreboard
# DONE Add difficulty level, (increased speed)

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
car_manager = CarManager()
screen = Screen()
score = Scoreboard()

screen.setup(width=600, height=500)
screen.tracer(0)
screen.listen()
screen.onkey(player.movement, "Up")

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    car_manager.create_car()
    car_manager.movement()

# Detecting vehicle collision:
    for all_cars in car_manager.cars:
        if all_cars.distance(player) < 25:
            game_is_on = False
            screen.clear()
            score.update_scoreboard()
            score.game_over()

# Detect level complete. Trigger next level:
    if player.distance(0, +240) < 5:
        score.increment_score()
        player.next_level()
        car_manager.increase_difficulty()

    screen.update()

screen.exitonclick()
