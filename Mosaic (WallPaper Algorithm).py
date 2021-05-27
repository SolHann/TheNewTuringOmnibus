import turtle

WIDTH, HEIGHT = 500, 500

screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)


ball = turtle.Turtle()

ball.color("green")
ball.goto(0, 0)
ball.speed(0)
turtle.delay(0)
ball.ht()


size = int(WIDTH/6) # size is a function of the size of the screen
for i in range(size):
    for j in range(size):
        x = i * 49/size  # whatever number is entered here produces a different mosaic
        y = j * 49/size
        c = int(x*x + y*y)
        if c % 3 == 0:
            colour = "red"
        elif c % 3 == 1:
            colour = "DarkGreen"
        else:
            colour = "CornflowerBlue"
        print(c, colour)
        ball.penup()
        ball.goto(20 + i * 5, 33 + j * 5) # fudge for centering reasons
        ball.color(colour)
        ball.dot(colour)
        ball.pendown()








screen.exitonclick()