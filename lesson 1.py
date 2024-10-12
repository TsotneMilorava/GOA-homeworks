from turtle import*
speed(10)
width(5)
color("green")
#drawing a square
forward(210)
left(90)
forward(210)
left(90)
forward(210)
left(90)
forward(210)
left(180)
#drawing a door
color("purple")
penup()
goto(70,0)
pendown()
forward(110)
right(90)
forward(70)
right(90)
forward(110)
left(180)
penup()
goto(120,60)
pendown()
forward(5)
#drawing window N1(left one)
color("skyblue")
penup()
goto(20,120)
pendown()
begin_fill()
forward(50)
right(90)
forward(40)
right(90)
forward(50)
right(90)
forward(40)
end_fill()
color("black")
right(180)
forward(20)
left(90)
forward(50)
penup()
goto(20,145)
pendown()
right(90)
forward(40)
penup()
goto(20,120)
pendown()
forward(40)
left(90)
forward(50)
left(90)
forward(40)
left(90)
forward(50)
#drawing window N2(right one)
color("skyblue")
begin_fill()
penup()
goto(150,120)
pendown()
left(90)
forward(40)
left(90)
forward(50)
left(90)
forward(40)
left(90)
forward(50)
end_fill()
color("black")
left(90)
forward(40)
left(90)
forward(50)
left(90)
forward(40)
left(90)
forward(50)
penup()
goto(170,120)
pendown()
left(180)
forward(50)
penup()
goto(150,145)
pendown()
right(90)
forward(40)
#completed both windows, starting roof
color("red")
penup()
goto(0,210)
pendown()
left(90)
right(30)
begin_fill()
forward(210)
right(120)
forward(210)
end_fill()
#completed house, starting grass
width(15)
color("green")
penup()
goto(-500,-50)
pendown()
left(60)
forward(1000)
left(90)
#building a fence
penup()
color("brown")
goto(-400,-50)
pendown()
forward(70)
penup()
goto(-300,-50)
pendown()
forward(70)
penup()
goto(-200,-50)
pendown()
forward(70)
penup()
goto(-100,-50)
pendown()
forward(70)
penup()
goto(0,-50)
pendown()
forward(70)
penup()
goto(100,-50)
pendown()
forward(70)
penup()
goto(200,-50)
pendown()
forward(70)
penup()
goto(300,-50)
pendown()
forward(70)
penup()
goto(400,-50)
pendown()
forward(70)
penup()
goto(500,-50)
pendown()
forward(70)
right(90)
penup()
goto(-500,-10)
pendown()
forward(1000)
#building a cross
left(90)
penup()
goto(-350,-50)
pendown()
forward(250)
right(90)
penup()
goto(-400,150)
pendown()
forward(100)
right(45)
penup()
goto(-365,65)
pendown()
forward(47)
#project finished!






















































exitonclick()