import turtle
wn = turtle.Screen()
wn.title("Stress Cookie")
wn.bgcolor("#F5E1FD")


wn.register_shape("/Users/farhanarahman/Desktop/cookie.gif")

cookie = turtle.Turtle()
cookie.shape("/Users/farhanarahman/Desktop/cookie.gif")
cookie.speed(0)

clicks = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color("#96B9D0")
pen.penup()
pen.goto(0,400)
pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal")) 


wn.mainloop()

