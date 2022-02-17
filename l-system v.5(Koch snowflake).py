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
leo.pensize(4)
leo.speed(1)
leo.setpos(-WIDTH // 6, -HEIGHT // 6)
leo.color('gold')

# l-system settings
gens = 5
axiom = 'F++F++F'
charcter_1, rule_1 = 'F', 'F-F++F-F'
step = 600
angle = 60

def apply_rules(axiom):
    return ''.join([rule_1 if character == charcter_1 else 
                    character for character in axiom])


def get_result(gens, axiom):
    for gen in range(gens):
        axiom = apply_rules(axiom)
    return axiom

for gen in range(gens):
    turtle.pencolor('white')
    turtle.goto(-WIDTH // 2 + 30, - HEIGHT // 2 - 100)
    turtle.clear()
    turtle.write(f'generation: {gen}', align="left", 
                 font = ("Arial", 30, "normal"))
    leo.setheading(0)
    leo.goto(-WIDTH // 6, HEIGHT // 6)
    leo.clear()
    
    length = step / pow(3, gen)
    for character in axiom:
        if character == charcter_1:
            leo.forward(length)
        elif character == '+':
            leo.right(angle)
        elif character == '-':
            leo.left(angle)
            
    axiom = apply_rules(axiom)
    
screen.exitonclick()