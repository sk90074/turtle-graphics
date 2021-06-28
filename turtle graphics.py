#Importing modules
import random
import turtle

#Functions
def evennumberloop(angle,randnum):
    for count in range(0,36):
        for count in range(0,randnum):
            t.forward(50)
            t.right(angle)
            t.color(random.randint(0,1), random.randint(0,1), random.randint(0,1))
        t.left(10)

def oddnumberloop(angle,randnum,size):
    for count in range(0,largestShape):
            for count in range(1,randnum):
                t.forward(size)
                t.right(angle)
                t.color(random.randint(0,1), random.randint(0,1), random.randint(0,1))

                size = size + 1
    

t = turtle.Pen()


#Loops for the program
for count in range(0,4):
    randnum = random.randint(3,8)
    angle = 360/randnum
    largestShape = 10*randnum
    size = 10
    if randnum % 2 == 0:
        evennumberloop(angle,randnum)
    else:
        oddnumberloop(angle,randnum,size)
        
    t.clear()
