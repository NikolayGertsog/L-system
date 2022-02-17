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
leo.pensize(3)
leo.speed(0)
leo.color('orange')

# l-system settings
gens = 20
axiom = 'A'
charcter_1, rule_1 = 'A', 'AB'
charcter_2, rule_2 = 'B', 'A'
step = 50
angle = 60

def apply_rules(axiom):
    return ''.join([rule_1 if character == charcter_1 else rule_2 for character in axiom])


def get_result(gens, axiom):
    for gen in range(gens):
        axiom = apply_rules(axiom)
    return axiom


turtle.pencolor('white')
turtle.goto(-WIDTH // 2 + 30, - HEIGHT // 2 + 30)
turtle.clear()
turtle.write(f'generation: {gens}', font = ("Arial", 30, "normal"))

axiom = get_result(gens, axiom)
for character in axiom:
    if character == charcter_1:
        leo.left(60)
        leo.forward(step)
    elif character == charcter_2:
        leo.right(60)
        leo.forward(step)

    
screen.exitonclick()