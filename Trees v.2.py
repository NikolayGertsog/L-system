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
axiom = '2222110'
axiom_temp = ''
step = 12 # Количество итераций(генераций)
angle = 20 # Угол
part = 5 # Длина сегмента
stack = []

# Dictionary tree forms:
F_Tree = {'1':'21',
          '0':'1[-22+1-0]+1-22+0'}

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
        turtle.right(angle - randint(-13, 13)) # Шаг направо(угол)      
    elif character == '-':
        turtle.left(angle - randint(-13, 13)) # Шаг налево(угол)
    elif character == '2':
        if randint(0, 10) > 4:
            turtle.forward(part) # Шаг прямо(длина)       
    elif character == '1':
        if randint(0, 10) > 4:
            turtle.forward(part) # Шаг прямо(длина)
    elif character == '0': # Листья
        stack.append(turtle.pensize()) # Сохраняем толищину в стек
        l = randint(5, 10)
        if l == 5:
            turtle.pensize(5)
        elif l == 6:
            turtle.pensize(6)
        elif l == 7:
            turtle.pensize(7)
        elif l == 8:
            turtle.pensize(8)
        elif l == 9:
            turtle.pensize(9)
        else:
            turtle.pensize(10)
            
        c = randint(1, 10)
        if c == 1:
            turtle.pencolor('#007000')
        elif c == 2:
            turtle.pencolor('#007900')
        elif c == 3:
            turtle.pencolor('#008000')
        elif c == 4:
            turtle.pencolor('#008900')
        elif c == 5:
            turtle.pencolor('#009000')
        elif c == 6:
            turtle.pencolor('#009900')
        elif c == 7:
            turtle.pencolor('#95b30a')
        elif c == 8:
            turtle.pencolor('#a1c10b')
        elif c == 9:
            turtle.pencolor('#304d04')
        else:
            turtle.pencolor('#426b06')
            
        p = randint(1, 10)
        if p == 1:
            turtle.forward(part - 1)
        elif p == 2:
            turtle.forward(part - 1.25)
        elif p == 3:
            turtle.forward(part - 1.5)
        elif p == 4:
            turtle.forward(part - 1.75)
        elif p == 5:
            turtle.forward(part - 2)
        elif p == 6:
            turtle.forward(part + 1)
        elif p == 7:
            turtle.forward(part + 1.25)
        elif p == 8:
            turtle.forward(part + 1.5)
        elif p == 9:
            turtle.forward(part + 1.75)
        else:
            turtle.forward(part + 2)
        turtle.pensize(stack.pop())
        turtle.pencolor('#000000')
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