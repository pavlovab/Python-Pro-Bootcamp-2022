import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Turtle Crossing Game")
screen.tracer(0)

turtle = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(fun=turtle.move, key="Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()


    #Detect crossing finish line.
    crossed_finish = turtle.crossed_finish_line()
    if crossed_finish:
        scoreboard.next_level()
        car_manager.increase_speed()

    #Detect collision with car.
    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            scoreboard.game_over()
            game_is_on = False 




screen.exitonclick()