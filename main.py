from turtle import Screen
import time
from snake import Snake
from food import Food
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

starting_position = [(0, 0), (-20, 0), (-40, 0)]
segments = []

snake = Snake()
food = Food()

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

screen.exitonclick()
