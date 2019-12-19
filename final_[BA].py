#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name
# Blake Allison
#Date
# 12/19/19

#make instructions
import turtle 
turtle.penup()
turtle.ht()
turtle.goto(-475, 375)
turtle.write("up, down, left, and right move as expected.", font=("Arial", 25, "bold"))
turtle.goto(-475, 350)
turtle.write("Space bar clears what you have drawn.", font=("Arial", 25, "bold"))
turtle.goto(-475, 330)
turtle.write("m draws a maze, g lets you go to the begining of that maze, and c deletes it.", font=("Arial", 15, "bold"))
turtle.goto(-475, 300)
turtle.write("u lifts the pen up and puts it down.", font=("Arial", 25, "bold"))
turtle.goto(-475, 285)
turtle.write("o makes the pen bigger p makes the pen smaller i changes the pens color.", font=("Arial", 15, "bold"))
turtle.goto(-475, 250)
turtle.write("h hides your drawer and s makes it appear.", font=("Arial", 25, "bold"))
turtle.goto(-475, 225)
turtle.write("0 draws a circle.", font=("Arial", 25, "bold"))
turtle.goto(-475, 200)
turtle.write("press 1 to delete this message.", font=("Arial", 25, "bold"))

# import stuff to draw a maze
import turtle as trtl 
franklin = trtl.Turtle()
#create a function to draw a maze
def draw_maze():
    franklin.penup()
    franklin.goto(0,0)
    franklin.pendown()
    franklin.speed(0)
    franklin.pensize(5)
    franklin.ht()
    crash = trtl.Turtle()
    crash.shape("turtle")
    crash.speed(0)
    crash_size = 1
    crash.shapesize(crash_size)
    crash.pensize(crash_size)
    crash.ht()

    #import 
    # om function so you can randomize maze and colors
    import random

    #name parts of your maze
    wall_size = 20
    gap_size = 50
    counter = 25
    franklin.penup()

    #define a thing to make a barrier
    def make_barrier():
        franklin.left(90)
        franklin.forward(40)
        franklin.back(40)
        franklin.right(90)

    #define a thing to create door
    def make_door():
        franklin.penup()
        franklin.forward(gap_size)
        franklin.pendown()


    def go_down():
        global crash_size
        crash.setheading(90)
        crash.forward(5)
        rad_colors = ["silver", "dark grey", "grey", "dim grey", "black", "light slate grey", "slate grey", "navy", "medium blue", "deep sky blue", "dodger blue", "dark turquoise", "deep pink", "pale violet red", "hot pink", "dark magenta", "medium violet red", "dark violet", "indigo", "medium purple", "chocolate", "sienna", "maroon", "firebrick", "lime", "crimson", "brown", "orange red", "lawn green", "forest green", "dark sea green"]
        color = random.choice(rad_colors)
        crash.pencolor(color)
        crash.stamp()
        color = random.choice(rad_colors)
        crash.color(color)


    # create maze and hide your moving turtle
    crash.ht()
    while (counter >= 0):
        if counter < 21:
            #randomize gap and wall placement
            door = random.randint(gap_size, wall_size - gap_size)
            barrier = random.randint(gap_size, wall_size - gap_size)

        #make colors to be randomly chosen have your walls become those colors
            rad_colors = ["silver", "dark grey", "grey", "dim grey", "black", "light slate grey", "slate grey", "navy", "medium blue", "deep sky blue", "dodger blue", "dark turquoise", "deep pink", "pale violet red", "hot pink", "dark magenta", "medium violet red", "dark violet", "indigo", "medium purple", "chocolate", "sienna", "maroon", "firebrick", "lime", "crimson", "brown", "orange red", "lawn green", "forest green", "dark sea green"]
            color = random.choice(rad_colors)
            franklin.pencolor(color)
            franklin.pendown()

        #based on what is drawn first draw things in a certain order
            if (door > barrier):
                franklin.forward(barrier)
        #make sure it doesnt draw barrier on the last or first few lines in maze
                if (counter <= 19):
                    if (counter >= 1):
                        make_barrier()
                franklin.forward(door-barrier)
        #make sure it doesn't create a door on the outer walls of the maze
                if (counter >= 4):
                    make_door()
                else:
                    franklin.forward(gap_size)
                franklin.forward(wall_size-door-gap_size)
                franklin.left(90)

        
            else:
                franklin.forward(door)
        #make sure it doesn't create a door on the outer walls of the maze
                if (counter >= 4):
                    make_door()
                else:
                    franklin.forward(gap_size)
                franklin.forward(barrier-door-gap_size)
        #make sure it doesnt draw barrier on the last or first few lines in maze
                if (counter <= 19):
                    if (counter >= 1):
                        make_barrier()
                franklin.forward(wall_size-barrier)
                franklin.left(90)
        wall_size += 20
        counter -= 1 


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#All code must be commented
#BONUS

#feature to change colors
import random  
def true_colors():
    rad_colors = ["silver", "dark grey", "grey", "dim grey", "black", "light slate grey", "slate grey", "navy", "medium blue", "deep sky blue", "dodger blue", "dark turquoise", "deep pink", "pale violet red", "hot pink", "dark magenta", "medium violet red", "dark violet", "indigo", "medium purple", "chocolate", "sienna", "maroon", "firebrick", "lime", "crimson", "brown", "orange red", "lawn green", "forest green", "dark sea green"]
    color = random.choice(rad_colors)
    drawer.pencolor(color)
    drawer.color(color)

#import required libraries
import turtle as trtl

#create turtle
drawer = trtl.Turtle()
drawer.pensize(5)
drawer.turtlesize(5)
bob = trtl.Turtle()
bob.ht()
bob.penup()

#movement functions
def go_up():
    drawer.setheading(0)
    drawer.forward(20)

def go_down():
    drawer.setheading(270)
    drawer.forward(20)

def go_left():
    drawer.setheading(180)
    drawer.forward(20)

def go_right():
    drawer.setheading(90)
    drawer.forward(20)

# pen up or down function
def pen_change():
    if (drawer.isdown() == True):
        drawer.penup()
    else:
        drawer.pendown()


#pensize change function
pensizes = 3
def get_big():
    global pensizes
    pensizes += 1
    drawer.pensize(pensizes)
    drawer.turtlesize(pensizes)
    bob.clear()
#stop pen from getting to a size of 0
def get_small():
    global pensizes
    if (pensizes != 1 and pensizes >= 1):
        pensizes -= 1
        drawer.pensize(pensizes)
        drawer.turtlesize(pensizes)
    else:
        bob.goto(-375, 275)
        bob.write ("Can't get smaller", font=("Arial", 25, "bold"))

# create function that draws a circle for you
def create_circle():
    drawer.circle(5)

# define a function that will send the turtle to the begining of the maze
def goto_maze_start():
    global franklin
    drawer.penup()
    xor = franklin.xcor()
    yor = franklin.ycor()
    drawer.goto(xor, yor)
    drawer.pendown()

#create a function that will clear the maze
def maze_clear():
    franklin.clear()

#create screen
wn = trtl.Screen()

#bind to keypresses
wn.onkeypress(go_up, "Right")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_right, "Up")
wn.onkeypress(go_left, "Left")
wn.onkeypress(drawer.clear, "space")
wn.onkeypress(pen_change, "u")
wn.onkeypress(get_big,"o")
wn.onkeypress(get_small,"p")
wn.onkeypress(true_colors, "i")
wn.onkeypress(create_circle, "0")
wn.onkeypress(draw_maze, "m")
wn.onkeypress(drawer.ht, "h")
wn.onkeypress(drawer.st, "s")
wn.onkeypress(goto_maze_start, "g")
wn.onkeypress(maze_clear, "c")
wn.onkeypress(turtle.clear, "1")

#listen
wn.listen()

#mainloop
wn.mainloop()