import turtle

turtle.pensize(3)
turtle.penup()
turtle.goto(-200, -50)
turtle.pendown()
turtle.circle(40, steps = 3) # 삼각형을 그린다

turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()
turtle.circle(40, steps = 4) # 사각형을 그린다

turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.circle(40, steps = 5) # 오각형을 그린다

turtle.penup()
turtle.goto(100, -50)
turtle.pendown()
turtle.circle(40, steps = 6) # 육각형을 그린다

turtle.penup()
turtle.goto(200, -50)
turtle.pendown()
turtle.circle(40,) # 원을 그린다

turtle.done()