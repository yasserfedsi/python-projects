from turtle import *

setup(400, 200) #Drawing the rectangle
penup()
goto(-200,100)
pendown()

# Drawing the black section
color("black")
begin_fill()
forward(400)
right(90)
forward(70)
right(90)
forward(400)
right(180)
end_fill()

# Drawing the white section
color("white")
begin_fill()
forward(400)
right(90)
forward(70)
right(90)
forward(400)
right(180)
end_fill()

# Drawing the green section
color("green")
begin_fill()
forward(400)
right(90)
forward(70)
right(90)
forward(400)
right(150)
end_fill()

# Drawing the red section
color("red")
begin_fill()
forward(200)
left(118)
forward(205)
end_fill()
mainloop()