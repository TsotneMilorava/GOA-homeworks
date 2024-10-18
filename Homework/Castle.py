from turtle import *
#create field
color("green")
speed(5)
width(5)
begin_fill()
penup()
goto(-500,-50)
pendown()
forward(1000)
right(90)
forward(450)
right(90)
forward(1000)
right(90)
forward(450)
end_fill()
#begin castle N1 tower
color("grey")
begin_fill()
penup()
goto(-400,-50)
pendown()
forward(200)
right(90)
forward(100)
right(90)
forward(200)
end_fill()
color("black")
left(180)
penup()
goto(-400,-50)
pendown()
forward(200)
right(90)
forward(100)
right(90)
forward(200)
color("grey")
begin_fill()
penup()
goto(-450,150)
pendown()
left(90)
forward(200)
left(90)
forward(40)
left(90)
forward(200)
left(90)
forward(40)
end_fill()
color("black")
left(90)
left(180)
penup()
goto(-400,150)
pendown()
forward(50)
right(90)
forward(40)
right(90)
forward(200)
right(90)
forward(40)
right(90)
forward(50)
right(90)
color("grey")
begin_fill()
penup()
goto(-400,190)
pendown()
forward(100)
right(90)
forward(100)
right(90)
forward(100)
end_fill()
color("black")
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
#building roof on N1 tower
color("grey")
begin_fill()
penup()
goto(-400,290)
pendown()
left(150)
forward(100)
right(120)
forward(100)
end_fill()
right(120)
color("black")
forward(100)
right(120)
forward(100)
right(120)
forward(100)
right(30)
forward(100)
# flag on N1 tower
left(180)
penup()
goto(-350,375)
pendown()
forward(50)
right(120)
#building second part of castle
color("gray")
penup()
goto(-300,-50)
pendown()
begin_fill()
left(30)
forward(600)
left(90)
forward(150)
left(90)
forward(600)
end_fill()
color("black")
left(90)
forward(150)
left(180)
forward(150)
right(90)
forward(600)
right(90)
forward(150)
#building second tower
color("gray")
begin_fill()
left(180)
forward(200)
left(90)
forward(50)
right(90)
forward(40)
right(90)
forward(200)
right(90)
forward(40)
right(90)
forward(50)
left(90)
forward(200)
end_fill()
color("black")
left(180)
forward(200)
right(90)
forward(50)
left(90)
forward(40)
left(90)
forward(200)
left(90)
forward(40)
left(90)
forward(50)
right(90)
forward(200)
left(180)
penup()
goto(300,190)
pendown()
color("gray")
begin_fill()
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
end_fill()
color("black")
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
#building roof on second tower
penup()
goto(300,290)
pendown()
color("gray")
begin_fill()
left(180)
left(60)
forward(100)
right(120)
forward(100)
end_fill()





























































































































































































































































exitonclick()