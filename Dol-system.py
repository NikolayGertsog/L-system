import turtle

# turtle settings:
turtle.hideturtle()
turtle.tracer(0)
turtle.penup()
turtle.setposition(0, -300) # Направление вверх
turtle.left(90)
turtle.pendown()
turtle.pensize(2)

# Rules:
#p1 : ar(a) → albr
#p2 : al(i) → blar
#p3 : br(b) → ar
#p4 : bl(l) → al

# l-system settings:
axiom = 'a'
axiom_temp = ''
step = 5 # generation
angle = 20
part = 5
stack = []

# Dictionary tree forms:
F_Tree = {'a':'ib', 'i':'ba', 'b':'a', 'l':'i'}

for i in range(step):
    for character in axiom:
        if character in F_Tree:
            axiom_temp += F_Tree[character]
        else:
            axiom_temp += character
    axiom = axiom_temp
    axiom_temp = ''
        
for character in axiom:
    if character == 'a':
        turtle.right(part * 2)  
    elif character == 'b':
        turtle.right(part)       
    elif character == 'i':
        turtle.left(part * 2)
    elif character == 'l':
        turtle.left(part)
turtle.update()
turtle.mainloop()