from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard


screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")

screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")


game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #DETECT COLLISION WITH FOOD
    if snake.head.distance(food) <18:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #DETECT COLLISION WITH WALL
    if snake.head.xcor() >290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() <-290:
        scoreboard.reset()
        snake.reset()

    #DETECT THE COLLISION WITH TAIL
    for segment in snake.segments[1:]:
        if segment ==snake.segments:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()



screen.exitonclick()