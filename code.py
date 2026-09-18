"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange, choice
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Cambia la dirección de la serpiente."""
    aim.x = x
    aim.y = y


def inside(head):
    """Comprueba si una posición está dentro de los límites."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move_food():
    """Mueve la comida un paso aleatorio válido."""
    directions = [
        vector(10, 0),
        vector(-10, 0),
        vector(0, 10),
        vector(0, -10),
    ]

    options = []

    for direction in directions:
        position = food.copy()
        position.move(direction)

        if inside(position) and position not in snake:
            options.append(position)

    if options:
        position = choice(options)
        food.x = position.x
        food.y = position.y


def new_food():
    """Coloca comida en una posición libre."""
    options = [
        vector(x, y)
        for x in range(-190, 190, 10)
        for y in range(-190, 190, 10)
        if vector(x, y) not in snake
    ]

    if not options:
        return False

    position = choice(options)
    food.x = position.x
    food.y = position.y
    return True


def move():
    """Mueve la serpiente y actualiza la comida."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)
    won = False

    if head == food:
        print('Snake:', len(snake))
        won = not new_food()
    else:
        snake.pop(0)
        move_food()

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    if won:
        print('¡Ganaste!')
    else:
        square(food.x, food.y, 9, 'green')

    update()

    if not won:
        ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()

onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

move()
done()