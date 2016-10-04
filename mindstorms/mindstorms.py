import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()

    brad.shape("circle")
    brad.color("yellow")
    brad.speed(4)

    draw_square(brad)
    
    angie = turtle.Turtle()

    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
    

    window.exitonclick()
    
draw_art()
