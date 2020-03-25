import turtle

# def Window():

wn = turtle.Screen()
wn.title("碰碰球")
wn.bgcolor("black") # 用白色试试
wn.setup(width=800, height=600)
wn.tracer(0)    # 防止游戏更新

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

#
def paddle_a_up()

# if __name__ == '__main__':
#     Window()
# 游戏主循环
while True:
    wn.update() # 每次循环更新屏幕