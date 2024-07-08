# draws a tree
import turtle

# set the canvas window
def set_canvas():
    s = turtle.Screen()     
    s.setup(450, 410)
    s.bgcolor('ivory')
    s.title('Turtle Program')
    return s

# set a turtle (a pen)
def set_pen(color):         
    t = turtle.Turtle()
    t.shape('turtle')  
    t.pen(pencolor=color,fillcolor=color, pensize=1, speed=30)
    return t

def draw_tree(branches, n):
  for i in range(branches): 
        t.color('olive drab')
        t.goto(0, 0)
        t.pendown()
        t.pensize(n)
        t.forward(60)
        t.left(30)
        t.forward(60)
        t.penup()
        t.right(20)
        t.pendown()
        t.color('pale green')
        t.dot(15)
        t.penup()
        i += 1
  for i in range(2 *branches):
        t.color('olive drab')
        t.goto(0, 0)
        t.pendown()
        t.pensize(n)
        t.forward(60)
        t.right(30)
        t.forward(60)
        t.penup()
        t.left(20)
        t.pendown()
        t.color('pale green')
        t.dot(15)
        t.penup()
        i += 1
  t.penup()      
  t.goto(0, 0)
  t.pensize(50)
  t.right(80)
  t.color('sienna')
  t.pendown()
  t.forward(100) 
        

# main program
s = set_canvas()
t = set_pen('olive drab')
t.penup()
t.left(90)
t.pendown()
draw_tree(10, 3)
turtle.done()
