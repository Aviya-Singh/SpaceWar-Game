#Title: Space War Game / Written in Python 3.11.3
#Author: Aviya Singh
#Date: November 20, 2023
#Module: Part I - Getting Started

#Import the modules
import os
import random
import turtle

#Required by MacOS to show the window 
turtle.fd(0)        
#Set the speed of the animation, 0 is the maximum speed                    
turtle.speed(0)    
#Change the background color                     
turtle.bgcolor("Brown")  
#Hide turtle               
turtle.ht()        
#Limit amount of memory used by turtle                     
turtle.setundobuffer(1)  
#Speeds up animation or drawing               
turtle.tracer(1)                        

class Sprite(turtle.Turtle):            #Inherit from the turtle module
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape=spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx, starty)
        self.speed=1

    def move(self):
        self.fd(self.speed)

        #Boundary detection
        if self.xcor() > 290:
            self.setx(290)
            self.rt(60)

        if self.xcor() < -290:
            self.setx(-290)
            self.rt(60)

        if self.ycor() > 290:
            self.sety(290)
            self.rt(60)

        if self.ycor() < -290:
            self.sety(-290)
            self.rt(60)

    def is_collision(self,other):
        if (self.xcor() >= (other.xcor() - 20)) and \
        (self.xcor() <= (other.xcor() + 20)) and \
        (self.ycor() >= (other.ycor() - 20)) and \
        (self.ycor() <= (other.ycor() + 20)):
            return True
        else:
            return False

class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed=4
        self.lives=3

    def turn_left(self):
        self.lt(45)

    def turn_right(self):
        self.rt(45)

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -= 1

class Enemy(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 6
        self.setheading(random.randint(0,360))
        self.goto(-1000,1000)

class Missile(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.3,stretch_len=0.3,outline=None)
        self.speed = 20
        self.status = "ready"

    def fire(self):
        if self.status == "ready":
            self.goto(player.xcor(),player.ycor())
            self.setheading(player.heading())
            self.status = "firing"

    def move(self):
        if self.status == "ready":
            self.goto(-1000,1000)

        if self.status == "firing":
            self.fd(self.speed)

        #Border check
        if self.xcor() < -290 or self.xcor() > 290 or \
            self.ycor() < -290 or self.ycor() > 290:
             self.goto(-1000,1000)
             self.status = "ready"
             

class Game():
    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = "playing"
        self.pen = turtle.Turtle()
        self.lives = 3

    def draw_border(self):
        #Draw border
        self.pen.speed(0)                       #Animation speed
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-300,300)
        self.pen.pendown()
        for side in range(4):
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()
        self.pen.ht()

#Create game object
game = Game()

#Draw the game border
game.draw_border()
            

#Create my sprites
player=Player("triangle","white",0,0)
enemy=Enemy("circle","black",-100,0)
missile=Missile("triangle","yellow",0,0)

#Keyboard bindings
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.decelerate, "Down")
turtle.onkey(missile.fire, "space")
turtle.listen()

#Main game loop
while True:
    player.move()
    enemy.move()
    missile.move()

    #Check for collision
    if player.is_collision(enemy):
        x = random.randint(-250,250)
        y = random.randint(-250,250)
        enemy.goto(x,y)

    #Check for collision between missile and enemy
    if missile.is_collision(enemy):
        x = random.randint(-250,250)
        y = random.randint(-250,250)
        enemy.goto(x,y)
        missile.status = "ready"


delay = input("Press enter to finish. >")