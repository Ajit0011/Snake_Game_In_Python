import turtle
import random
import time

delay = 0.1
score = 0
highest_score = 0

#snake_bodies
bodies = []

#getting_a_screen_or_canvas
s = turtle.Screen()
s.title("Snake Game!!")
s.bgcolor("grey")
s.setup(width=600,height=600)

#Draw_border
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
mypen.color("red")
for side in range(2):
    mypen.forward(597)
    mypen.left(90)
    mypen.color("red")
for side in range(2):
    mypen.color("green")
    mypen.forward(597)
    mypen.left(90)    
mypen.hideturtle()

#create_snake_head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("white")
head.fillcolor("red")
head.penup()
head.goto(0,0)
head.direction = "stop"

#snake_food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.fillcolor("green")
food.penup()
food.ht()
food.goto(0,200)
food.st()

#score_board
sb = turtle.Turtle()
sb.shape("square")
sb.fillcolor("black")
sb.penup()
sb.ht()
sb.goto(-250,-250)
sb.write("Score:0  |  highest Score: 0")

def moveup():
    if head.direction != "down":
        head.direction = "up"
def movedown():
    if head.direction != "up":
        head.direction = "down"
def moveleft():
    if head.direction != "right":
        head.direction = "left"
def moveright():
    if head.direction != "left":
        head.direction = "right"  
def movestop():
    head.direction = "stop"
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)   
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)   

#event_handling_key_mappings
s.listen()
s.onkey(moveup, "Up")
s.onkey(moveup, "W")
s.onkey(moveup, "w")
s.onkey(movedown, "Down")
s.onkey(movedown, "S")
s.onkey(movedown, "s")
s.onkey(moveleft, "Left")
s.onkey(moveleft, "A")
s.onkey(moveleft, "a")
s.onkey(moveright, "Right")
s.onkey(moveright, "D")
s.onkey(moveright, "d")
s.onkey(movestop, "space")

#main_loop
while True:
    s.update()  #this_is_to_update_the_screen
    #check_collision_with_border
    if head.xcor() > 290:
        head.setx(-290)
    if head.xcor() < -290:
        head.setx(290)
    if head.ycor() > 290:
        head.sety(-290)    
    if head.ycor() < -290:
        head.sety(290)

    #check_collision_with_food
    if head.distance(food) < 20:
        #move_the_food_to_new_random_place
        x = random.randint(-290, 290) 
        y = random.randint(-290, 290)  
        food.goto(x,y) 

        #increase_the_length_of_the_snake
        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("circle")
        body.color("red")
        body.fillcolor("grey")
        bodies.append(body)  #append_new_body

        #increase_the_score
        score += 1

        #change_delay
        delay -= 0.001

        #update_the_highest_score
        if score > highest_score:
            highest_score = score
        sb.clear()
        sb.write("Score: {} Highest Score: {}".format(score,highest_score))

    #move_the_snake_bodies
    for index in range(len(bodies)-1,0,-1):
        x = bodies[index-1].xcor() 
        y = bodies[index-1].ycor()
        bodies[index].goto(x,y)

    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)
    move()

    #check_collision_with_snake_body
    for body in bodies:
        if body.distance(head) <20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            #hide_bodies
            for body in bodies:
                body.ht()
            bodies.clear()

            score = 0
            delay = 0.1

            #update_score_board
            sb.clear()
            sb.write("Score: {} Highest Score: {}".format(score,highest_score))
    time.sleep(delay)
s.mainloop()                        


