import re
import turtle
from random import randint

# screen settings
WIDTH, HEIGHT = 1200, 800
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.screensize(1 * WIDTH, 1 * HEIGHT)
screen.bgpic('moon.gif')
screen.delay(0)

# turtle settings
leo = turtle.Turtle()
leo.pensize(3)
leo.speed(0)
leo.penup()
leo.setpos(WIDTH // 6, -HEIGHT // 4 - 25)
leo.pendown()
leo.color('green')

# l-system settings
gens = 13
axiom = 'XY'
charcter_1, rule_1 = 'X', 'F[@[-X]+X]'
step = 85
angle = lambda: randint(0, 45)
stack = []
color = [0.35, 0.2, 0.0]
thickness = 20

def apply_rules(axiom):
    return ''.join([rule_1 if character == charcter_1 else
                    character for character in axiom])

def get_result(gens, axiom):
    for gen in range(gens):
        axiom = apply_rules(axiom)
    return axiom

axiom = get_result(gens, axiom)
leo.left(90)
leo.pensize(thickness)
for character in axiom:
    leo.color(color)
    if character == 'F' or character == 'X':
        leo.forward(step)
        
    elif character == '@':
        step -= 6
        color[1] += 0.04
        thickness -= 2
        thickness = max(1, thickness)
        leo.pensize(thickness)
        
    elif character == '+':
        leo.right(angle())
        
    elif character == '-':
        leo.left(angle())
        
    elif character == '[':
        angle_, pos_ = leo.heading(), leo.pos()
        stack.append((angle_, pos_, thickness, step, color[1]))
        
    elif character == ']':
        angle_, pos_, thickness, step, color[1] = stack.pop()
        leo.pensize(thickness)
        leo.setheading(angle_)
        leo.penup()
        leo.goto(pos_)
        leo.pendown()

screen.exitonclick()