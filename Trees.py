import turtle

# turtle settings:
turtle.hideturtle()
turtle.tracer(0)
turtle.penup()
turtle.setposition(0, -300) # Направление вверх
turtle.left(90)
turtle.pendown()
turtle.pensize(2)

# l-system settings:
axiom = '0'
axiom_temp = ''
step = 5 # Количество итераций(генераций)
angle = 45 # Угол
part = 20 # Длина сегмента
stack = []

# Dictionary tree forms:
F_Tree = {'1':'1', '0':'11[-0]+0'}

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
        turtle.right(angle) # Шаг направо(угол)      
    elif character == '-':
        turtle.left(angle) # Шаг налево(угол)       
    elif character == '1':
        turtle.forward(part) # Шаг прямо(длина)
    elif character == '0':
        turtle.forward(part) # Шаг прямо(длина)
    elif character == '[':
        stack.append(turtle.xcor()) # Добавить в стек X-координату
        stack.append(turtle.ycor()) # Добавить в стек Y-координату
        stack.append(turtle.heading()) # Добавить в стек угол поворота черепахи
    elif character == ']': # Возвращение черепахи на прежнее место
        turtle.penup()
        turtle.setheading(stack.pop()) # Возвращаем в обратной последовательности угол поворота черепахи
        turtle.sety(stack.pop()) # Y-координату
        turtle.setx(stack.pop()) # X-координату
        turtle.pendown()        
turtle.update()
turtle.mainloop()