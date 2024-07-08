import turtle

# size = length of a side
# n = angles
# times = how much depth we want in the dragon curve

# https://www.w3schools.com/python/python_lists_loop.asp
# ^ I used this to help me with my for-loop.

def dragon(size, n, times):
    t.pendown()
    if times > 0: # recursion call
        for i in [n , n * -2, n , 0]:
            dragon(size/3 , 90, times - 1)
            t.right(i)
            dragon(size/3 , 90, times - 1)
            t.left(i)
            dragon(size/3 , 90, times - 1)
            t.right(i)
    else: # base case 
        t.forward(size)
          

t = turtle.Turtle()
t.penup()
t.speed(-10)
t.goto(-100,100)

for i in range(3):
    dragon(366,90, 4)
    
turtle.done()