import re
import turtle

# screen settings
WIDTH, HEIGHT = 1200, 800
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.screensize(1 * WIDTH, 1 * HEIGHT)
screen.bgcolor('black')
screen.delay(0)

# turtle settings
leo = turtle.Turtle()
leo.pensize(2)
leo.speed(0)
leo.setpos(-WIDTH // 4, -HEIGHT // 4 - 25)
leo.color('magenta')

# l-system settings
gens = 13
axiom = 'XY'
charcter_1, rule_1 = 'X', 'X+YF+'
charcter_2, rule_2 = 'Y', '-FX-Y'
step = 4
angle = 90

def apply_rules(axiom):
    return ''.join([rule_1 if character == charcter_1 else 
                    rule_2 if character == charcter_2 else
                    character for character in axiom])


def get_result(gens, axiom):
    for gen in range(gens):
        axiom = apply_rules(axiom)
    return axiom


turtle.pencolor('white')
turtle.goto(-WIDTH // 2 + 30, - HEIGHT // 2 - 100)
turtle.clear()
turtle.write(f'generation: {gens}', font = ("Arial", 30, "normal"))

axiom = get_result(gens, axiom)
for character in axiom:
    if character == charcter_1 or character == charcter_2:
        leo.forward(step)
    elif character == '+':
        leo.right(angle)
    elif character == '-':
        leo.left(angle)

screen.exitonclick()