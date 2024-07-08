import turtle

# size = length of a side
# n = angles
# times = how many times we want the triangles to be made with the other triangles


# https://www.w3schools.com/python/python_lists_loop.asp
# ^ I used this to help me with my for-loop.

# A TA also helped clarify to me how the Koch snowflake should be made.

def snowflake(size, n, times):
    t.pendown()
    if times == 0: # base case
        t.forward(size)
    else:  # recursion call
        for i in [n , n * -2, n , 0]:
            snowflake(size/3 , 60, times - 1)
            t.left(i);
        
          

t = turtle.Turtle()
t.penup()
t.speed(-1)
t.goto(-100,100)

for i in range(3):
    snowflake(366,60, 4)
    t.right(120);
turtle.done()