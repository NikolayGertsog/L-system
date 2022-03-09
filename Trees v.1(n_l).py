import turtle
from random import randint

# turtle settings:
turtle.hideturtle()
turtle.tracer(0)
turtle.penup()
turtle.setposition(0, -300) # Направление вверх
turtle.left(90)
turtle.pendown()
thick = 16
turtle.pensize(thick)

# l-system settings:
axiom = '22220'
axiom_temp = ''
step = 11 # Количество итераций(генераций)
angle = 20 # Угол
part = 6.5 # Длина сегмента
stack = []

# Dictionary tree forms:
F_Tree = {'1':'21',
          '0':'11[-20]+20'}

for i in range(step):
    for character in axiom:
        if character in F_Tree:
            axiom_temp += F_Tree[character]
        else:
            axiom_temp += character
    axiom = axiom_temp
    axiom_temp = ''
        
for character in axiom:
    if character == '+':
        turtle.right(angle - randint(-13,13)) # Шаг направо(угол)      
    elif character == '-':
        turtle.left(angle - randint(-13,13)) # Шаг налево(угол)
    elif character == '2':
        if randint(0, 10) > 4:
            turtle.forward(part) # Шаг прямо(длина)       
    elif character == '1':
        turtle.forward(part) # Шаг прямо(длина)
    elif character == '0':
        turtle.forward(part) # Шаг прямо(длина)
    elif character == '[':
        thick = thick * 0.75 # Уменьшаем на четверть
        turtle.pensize(thick)
        stack.append(thick) # Добавляем толщину в стек
        stack.append(turtle.xcor()) # Добавить в стек X-координату
        stack.append(turtle.ycor()) # Добавить в стек Y-координату
        stack.append(turtle.heading()) # Добавить в стек угол поворота черепахи
    elif character == ']': # Возвращение черепахи на прежнее место
        turtle.penup()
        turtle.setheading(stack.pop()) # Возвращаем в обратной последовательности угол поворота черепахи
        turtle.sety(stack.pop()) # Y-координату
        turtle.setx(stack.pop()) # X-координату
        thick = stack.pop()
        turtle.pensize(thick)
        turtle.pendown()        
turtle.update()
turtle.mainloop()