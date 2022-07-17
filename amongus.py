import turtle
win =turtle.getscreen()
imposter=turtle.Turtle()
win.setup(width=600, height=600)

body_color='blue'
glass_color='#9acedc'



def body():
    imposter.pensize(20)
    imposter.fillcolor(body_color)
    imposter.begin_fill()
    imposter.right(90)
    imposter.forward(50)
    imposter.right(180)
    imposter.circle(40, -180)
    imposter.right(180)
    imposter.forward(200)

    imposter.right(180)
    imposter.circle(100, -180)

    imposter.backward(20)
    imposter.left(15)
    imposter.circle(500, -20)
    imposter.backward(20)

    imposter.circle(40,-180)
    imposter.left(7)
    imposter.backward(50)

    imposter.up()
    imposter.left(90)
    imposter.forward(10)
    imposter.right(90)
    imposter.down()
    imposter.right(240)
    imposter.circle(50, -70)

    imposter.end_fill()


def glass():
    imposter.up()
    imposter.right(230)
    imposter.forward(100)
    imposter.left(90)
    imposter.forward(20)
    imposter.right(90)

    imposter.down()
    imposter.fillcolor(glass_color)
    imposter.begin_fill()

    imposter.right(150)
    imposter.circle(90, -55)

    imposter.right(180)
    imposter.forward(1)
    imposter.right(180)
    imposter.circle(10, -65)
    imposter.right(180)
    imposter.forward(110)
    imposter.right(180) 

    imposter.circle(50, -190)    
    imposter.right(170)    
    imposter.forward(80)    

    imposter.right(180)    
    imposter.circle(45, -30)    

    imposter.end_fill()    


def backpack():
    imposter.up()
    imposter.right(60)
    imposter.forward(100)
    imposter.right(90)
    imposter.forward(75)

    imposter.fillcolor(body_color)
    imposter.begin_fill()

    imposter.down()
    imposter.forward(30)
    imposter.right(255)
    
    imposter.circle(300, -30)
    imposter.right(260)
    imposter.forward(30)
    
    imposter.end_fill()



body()
glass()
backpack()

turtle.done()