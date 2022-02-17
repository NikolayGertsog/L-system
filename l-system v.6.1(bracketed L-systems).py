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
leo.setpos(0, -HEIGHT // 2)
leo.color('green')

# l-system settings
gens = 6
axiom = 'XY'
charcter_1, rule_1 = 'F', 'FF'
charcter_2, rule_2 = 'X', 'F[+X]F[-X]+x'
step = 7
angle = 22.5
stack = []

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
leo.left(90)
for character in axiom:
    if character == charcter_1:
        leo.forward(step)
    elif character == '+':
        leo.right(angle)
    elif character == '-':
        leo.left(angle)
    elif character == '[':
        angle_, pos_ = leo.heading(), leo.pos()
        stack.append((angle_, pos_))
    elif character == ']':
        angle_, pos_ = stack.pop()
        leo.setheading(angle_)
        leo.penup()
        leo.goto(pos_)
        leo.pendown()

screen.exitonclick()