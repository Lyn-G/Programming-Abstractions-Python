#
# DRAW SHAPES
#
import turtle

# draw a star
def star(size, n):
    t.pendown()
    t.begin_fill()
    for i in range(n):
        t.forward(size);
        t.left(144);
        i += 1
    t.end_fill()

def star_recursive(size, n):
    t.pendown()
    # TA notes
    #t.begin_fill
    # base case (how our recursion ends)
    if n == 0:
        return 
    t.forward(size);
    t.left(144);
    star_recursive(size, n-1);

def polygon(size, n):
    t.pendown()
    t.begin_fill
    for i in range(n):
        t.forward(size);
        t.left(300);
        i += 1

def polygon_recursive(size, n):
    turtle.width(4)
    t.pendown()
    t.begin_fill
    if n == 0:
        return
    t.forward(size);
    t.left(300);
    polygon_recursive(size, n-1);
    
# main program
s = turtle.Screen()     # make a canvas window
s.setup(400, 400)
s.bgcolor("ivory4")
s.title("Turtle Program")

t = turtle.Turtle()     # make a pen
t.shape("turtle")  
t.pen(pensize=1, speed=0)

t.penup()
t.goto(120,150)        
t.color('medium sea green')
star(20, 5)

t.penup()
t.goto(-120,-150) 
t.color('lime')
star_recursive(30, 5)

t.penup()
t.goto(-80,50) 
t.color('medium spring green')
polygon(60,6)

t.penup()
t.goto(-150,180) 
t.color('forest green')
polygon_recursive(70,6)

t.penup()
t.home()
turtle.done()