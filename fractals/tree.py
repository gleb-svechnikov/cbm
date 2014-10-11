import turtle
import sys

def generate(n, result='[X]'):
    for _ in range(n):
        # rule #2
        result = result.replace('F', 'FF')
        # rule #1
        result = result.replace('X', 'F-[[X]+X]+F[+FX]-X')

    return result

def draw(cmds, size=2):
    stack = []
    for cmd in cmds:
        if cmd=='F':
            turtle.forward(size)
        elif cmd=='-':
            turtle.left(25)
        elif cmd=='+':
            turtle.right(25)
        elif cmd=='X':
            pass
        elif cmd=='[':
            stack.append((turtle.position(), turtle.heading()))
        elif cmd==']':
            position, heading = stack.pop()
            turtle.penup()
            turtle.setposition(position)
            turtle.setheading(heading)
            turtle.pendown()
        else:
            raise ValueError('Unknown Cmd: {}'.format(ord(cmd)))
    turtle.update()

def setup():
    turtle.hideturtle()
    turtle.tracer(1e3,0)
    turtle.left(90)
    turtle.penup()
    turtle.goto(0,-turtle.window_height()/2)
    turtle.pendown()

setup()
plant = generate(6)
draw(plant, 2)
turtle.exitonclick()
