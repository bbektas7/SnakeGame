from turtle import Screen,Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreBoard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_one = True
while game_is_one:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreBoard.increase_score()
    
    if snake.head.xcor()> 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280: 
        scoreBoard.reset()
        snake.reset()
        
    for seg in snake.segment[1:]: 
        if snake.head.distance(seg) < 10:
            scoreBoard.reset()
            snake.reset()

    


screen.exitonclick()