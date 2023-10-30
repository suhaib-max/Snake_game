from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreborad import ScoreBoard

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

starting_position = [(0, 0), (-20, 0), (-40, 0)]
segments = []

snake = Snake()
food = Food()
score_board = ScoreBoard()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# To run the game constantly we need to use while loop
game_is_on = True
while game_is_on:
    screen.update()  # to refresh or to redraw otherwise there is nothing on the screen
    # all segment goes move forward then only to refresh
    time.sleep(0.15)
    snake.move()
    # segment means each object that we are created before
    # detect coalition with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()
    # Dect collition
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score_board.game_over()

    for segment in snake.segments[1::]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()
    # if head colid any segment touch in the tail

screen.exitonclick()
