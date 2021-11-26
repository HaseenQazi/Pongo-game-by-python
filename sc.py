from turtle import Turtle , Screen
from pad import Padle
from ball import Ball
from score import Scoreboard
import time


sc=Screen()
sc.bgcolor('black')
sc.setup(width=800,height=600)
sc.title('PONG GAME CREATED BY UMAR AND HASIN')
sc.tracer(0)

rpad=Padle(350,0)
lpad=Padle(-350,0)
ball=Ball()
score=Scoreboard()


sc.listen()
sc.onkey(rpad.goup,'Up')
sc.onkey(rpad.godown,'Down')
sc.onkey(lpad.goup,'w')
sc.onkey(lpad.godown,'s')

game=True


while game:
    time.sleep(ball.move_s)
    sc.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    if ball.distance(rpad) < 50 and ball.xcor() > 320 or ball.distance(lpad) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    if ball.xcor() > 380:
        ball.rest_p()
        score.l_point()

    if ball.xcor() < -380:
        ball.rest_p()
        score.r_point()

    if score.l_score== 10:  
        game=False
        score.display('PLAYER A WIN')

    if score.r_score == 10:
        game=False
        score.display('PLAYER B WIN')

sc.exitonclick()