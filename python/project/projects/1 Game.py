import turtle
import winsound

# 游戏窗口:

wn = turtle.Screen()
wn.title("碰碰球")
wn.bgcolor("black") # 用白色试试
wn.setup(width=800, height=600)
wn.tracer(0)    # 防止游戏更新

# 得分
score_a = 0
score_b = 0

# 板子 A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square") # 板子形状
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# 板子 B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square") # 板子形状
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350, 0)

# 球
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square") # 板子形状
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.2
ball.dy = 0.2

# 积分器
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("选手A: 0   选手B: 0", align="center", font=("Courier", 24, "normal"))

# A目标向上
def paddle_a_up():
    y = paddle_a.ycor()     # 返回 y 坐标
    y += 20
    paddle_a.sety(y)
# A目标向下
def paddle_a_down():
    y = paddle_a.ycor()     # 返回 y 坐标
    y -= 20
    paddle_a.sety(y)

# B
def paddle_b_up():
    y = paddle_b.ycor()     # 返回 y 坐标
    y += 20
    paddle_b.sety(y)
# B 目标向下
def paddle_b_down():
    y = paddle_b.ycor()     # 返回 y 坐标
    y -= 20
    paddle_b.sety(y)


# 键盘控制，绑定，游戏控制
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# if __name__ == '__main__':
#     Window()
# 游戏主循环
while True:
    wn.update() # 每次循环更新屏幕

    # 移动球
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("选手A: {}   选手B: {}".format(score_a, score_b),align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("选手A: {}   选手B: {}".format(score_a, score_b),align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # 弹弹球
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 50 ) and ball.ycor()> paddle_b.ycor()-50:
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 50 ) and ball.ycor()> paddle_a.ycor()-50:
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)