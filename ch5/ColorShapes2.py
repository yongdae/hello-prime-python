import turtle

turtle.pensize(3) # 팬의 두께를 3픽셀로 설정
turtle.penup() # 펜을 들어올린다.
turtle.goto(-200, -50)
turtle.pendown() # 펜을 내려놓는다.
turtle.begin_fill() # 도형을 색상으로 채우기 시작
turtle.color("red")
turtle.setheading(60)
turtle.circle(40, steps = 3) # 삼각형을 그린다.
turtle.end_fill() # 도형을 색상으로 채운다.

turtle.penup() # 펜을 들어올린다.
turtle.goto(-100, -50)
turtle.pendown() # 펜을 내려놓는다.
turtle.begin_fill() # 도형을 색상으로 채우기 시작
turtle.color("blue")
turtle.setheading(45)
turtle.circle(40, steps = 4) # 사각형을 그린다.
turtle.end_fill() # 도형을 색상으로 채운다.

turtle.penup() # 펜을 들어올린다.
turtle.goto(0, -50)
turtle.pendown() # 펜을 내려놓는다.
turtle.begin_fill() # 도형을 색상으로 채우기 시작
turtle.color("green")
turtle.setheading(35)
turtle.circle(40, steps = 5) # 오각형을 그린다.
turtle.end_fill() # 도형을 색상으로 채운다.

turtle.penup() # 펜을 들어올린다.
turtle.goto(100, -50)
turtle.pendown() # 펜을 내려놓는다.
turtle.begin_fill() # 도형을 색상으로 채우기 시작
turtle.color("yellow")
turtle.setheading(30)
turtle.circle(40, steps = 6) # 육각형을 그린다.
turtle.end_fill() # 도형을 색상으로 채운다.

turtle.penup() # 펜을 들어올린다.
turtle.goto(200, -50)
turtle.pendown() # 펜을 내려놓는다.
turtle.begin_fill() # 도형을 색상으로 채우기 시작
turtle.color("purple")
turtle.setheading(25)
turtle.circle(40, steps = 8) # 팔각형을.
turtle.end_fill() # 도형을 색상으로 채운다.

turtle.penup() # 펜을 들어올린다.
turtle.goto(-130, 50)
turtle.pendown()
turtle.color("green")
turtle.write("화려한 형형색색의 도형", font = ("맑은 고딕", 18, "bold"))

turtle.hideturtle() # 펜을 숨긴다.

turtle.done()
