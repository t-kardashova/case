import turtle

turtlePen = turtle.Turtle()
window = turtle.Screen()
t = turtlePen
t.pencolor('white')
t.pensize(3)


def lft_rght_trngl(x1, y1, ctht):

    """ a right triangle looking to the left; ctht - cathet; x1, y1 - coordinates of the origin"""

    t.up()
    t.goto(x1, y1)
    t.down()
    t.fd(ctht)
    t.lt(90)
    t.fd(ctht)
    t.lt(45)
    t.goto(x1, y1)
    t.rt(135)


def rght_rght_trngl(x1, y1, ctht):

    """a right triangle looking to the right; ctht - cathet; x1, y1 - coordinates of the origin"""

    t.up()
    t.goto(x1, y1)
    t.down()
    t.rt(90)
    t.fd(ctht)
    t.lt(90)
    t.fd(ctht)
    t.lt(45)
    t.goto(x1, y1)
    t.rt(45)


def rght_trngl(x1, y1, ctht, ftng):

    """triangle looking to the right; ctht - cathet; x1, y1 - coordinates of the start; ftng - footing"""

    t.up()
    t.goto(x1, y1)
    t.down()
    t.lt(45)
    t.fd(ctht)
    t.lt(135)
    t.fd(ftng)
    t.rt(135)
    t.goto(x1, y1)
    t.rt(45)


def dwn_trngl(x1, y1, ctht, ftng):

    """a triangle looking to the up; ctht - cathet; x1, y1 - coordinates of the start, ftng - footing"""

    t.up()
    t.goto(x1, y1)
    t.down()
    t.lt(135)
    t.fd(ctht)
    t.lt(135)
    t.fd(ftng)
    t.rt(135)
    t.goto(x1, y1)
    t.rt(135)


def prl(x1, y1):

    """"
    Function that draws parallelogram, where x1, y1 is the origin down up
    """
    t.up()
    t.goto(x1, y1)
    t.down()
    t.rt(45)
    t.fd(70)
    t.rt(45)
    t.fd(100)
    t.rt(135)
    t.fd(70)
    t.rt(45)
    t.fd(100)
    t.rt(90)


def prl_rght(x1, y1):

    """"
    Function that draws parallelogram, where x1, y1 is the origin down up
    """
    t.up()
    t.goto(x1, y1)
    t.down()
    t.lt(45)
    t.fd(70)
    t.rt(45)
    t.fd(100)
    t.rt(135)
    t.fd(70)
    t.rt(45)
    t.fd(100)
    t.rt(90)



def sqr(x1, y2):
    """"
    Function that draws square, where x1, y2  is the coordinat of the start
    """
    t.up()
    t.goto(x1, y2)
    t.down()
    t.rt(90)
    t.fd(70)
    t.rt(90)
    t.fd(70)
    t.rt(90)
    t.fd(70)
    t.rt(90)
    t.fd(70)


def rhomb(x1, y1, ctht):
    t.up()
    t.goto(x1, y1)
    t.down()
    t.rt(45)
    t.fd(ctht)
    t.lt(90)
    t.fd(ctht)
    t.lt(90)
    t.fd(ctht)
    t.lt(90)
    t.fd(ctht)
    t.rt(45)


# Algorithm for the first picture.

t.fillcolor('cyan')
t.begin_fill()
t.lt(45)
prl(-700, 350)
t.end_fill()

t.fillcolor('pink')
t.begin_fill()
t.rt(45)
sqr(-490, 280)
t.end_fill()

t.fillcolor('lightgreen')
t.begin_fill()
lft_rght_trngl(-700, 105, 140)
t.end_fill()

t.fillcolor('violet')
t.begin_fill()
t.rt(90)
rght_rght_trngl(-560, 105, 140)
t.end_fill()

t.fillcolor('gold')
t.begin_fill()
t.rt(45)
rght_rght_trngl(-560, -35, 100)
t.end_fill()

t.fillcolor('lavender')
t.begin_fill()
t.rt(180)
dwn_trngl(-560, 35, 70, 100)
t.end_fill()

t.fillcolor('salmon')
t.begin_fill()
t.rt(45)
dwn_trngl(-510, 105, 70, 100)
t.end_fill()



# Algorithm for the second picture.

t.fillcolor('gold')
t.begin_fill()
rhomb(428, -60, -80)
t.end_fill()

t.fillcolor('pink')
t.begin_fill()
t.rt(90)
rght_rght_trngl(498, -130, -130)
t.end_fill()

t.fillcolor('pink')
t.begin_fill()
t.lt(90)
prl_rght(537, -190)
t.end_fill()

t.fillcolor('salmon')
t.begin_fill()
t.rt(360)
rght_rght_trngl(257, -370, -130)
t.end_fill()

t.fillcolor('gold')
t.begin_fill()
t.rt(315)
rght_rght_trngl(387, -398, -70,)
t.end_fill()

t.fillcolor('HotPink')
t.begin_fill()
t.rt(180)
dwn_trngl(410, -420, -45, -45)
t.end_fill()

t.fillcolor('HotPink')
t.begin_fill()
t.rt(45)
dwn_trngl(300, -402, -45, -45)
t.rt(90)
t.end_fill()


# Algorithm for the third picture.
t.fillcolor("blue")
t.begin_fill()
lft_rght_trngl(150, 0, 100)
t.end_fill()

t.fillcolor("aqua")
t.begin_fill()
prl_rght(250, 0)
t.end_fill()

t.fillcolor("aqua")
t.begin_fill()
rght_trngl(250, 100, 90, 127)
t.end_fill()

t.fillcolor("blue")
t.begin_fill()
rght_trngl(137, 113, -70, -100)
t.end_fill()

t.fillcolor("aqua")
t.begin_fill()
rhomb(172, 150, 70)
t.end_fill()

t.fillcolor("blue")
t.begin_fill()
rght_trngl(172, 249, 70, 100)
rght_trngl(172, 249, -70, -100)
t.lt(90)
t.end_fill()


# Algorithm for the fourth picture
t.fillcolor('lightgreen')
t.begin_fill()
t.lt(45)
prl(-700, -250)
t.end_fill()

t.fillcolor('gold')
t.begin_fill()
t.rt(-45)
rght_rght_trngl(-730, -235, 125)
t.end_fill()

t.fillcolor('salmon')
t.begin_fill()
t.rt(-45)
rght_rght_trngl(-600, -245, 110)
t.end_fill()

t.fillcolor('orange')
t.begin_fill()
t.rt(45)
rhomb(-520,-244,50)
t.end_fill()

t.fillcolor('violet')
t.begin_fill()
t.rt(45)
rght_rght_trngl(-525, -244, 47)
t.end_fill()

t.fillcolor('lightblue')
t.begin_fill()
t.rt(-180)
rght_rght_trngl(-624, -250, 100)
t.end_fill()

t.fillcolor('red')
t.begin_fill()
t.rt(180)
rght_rght_trngl(-450, -244, 47)
t.end_fill()

t.fillcolor('purple')
t.begin_fill()
t.rt(-135)
rght_rght_trngl(-600, -50, 35)
t.end_fill()


window.mainloop()
