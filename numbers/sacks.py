import turtle
import math

endVal = 10000   # max value to draw to
turtle.speed(0) # fastest=0, slowest=10, init=3
turtle.hideturtle() # speeds it up
turtle.delay(0)     # time between updates in ms

# some constants
goldenRatio = 1.618033988
goldenAngle = (math.pi * 2) / (goldenRatio**2)
log2 = math.log(2)


def point(x,y,c='black'):
    turtle.penup()
    turtle.setpos(x,y)
    turtle.color(c)
    turtle.dot(3)

def isPrime(n):
    #if (isNaN(n) || !isFinite(n) || n % 1 || n < 2) return false;
    if n % 1 or n < 2:
        return False
    if n == leastFactor(n):
        return True;
    return False;

def leastFactor(n):
    if n == 0: return 0
    if n % 1 or n * n < 2: return 1
    if n % 2 == 0: return 2
    if n % 3 == 0: return 3
    if n % 5 == 0: return 5
    m = math.sqrt(n)
    for i in xrange(7, int(m)+1, 30):
        if n % i == 0: return i
        if n % (i + 4) == 0: return i + 4
        if n % (i + 6) == 0: return i + 6
        if n % (i + 10) == 0: return i + 10
        if n % (i + 12) == 0: return i + 12
        if n % (i + 16) == 0: return i + 16
        if n % (i + 22) == 0: return i + 22
        if n % (i + 24) == 0: return i + 24
    return n

for i in xrange(1, endVal, 2):
    #Calculate the next coordinate
    if isPrime(i):
        r = 3 * math.sqrt(i)
        theta = i * goldenAngle
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        point(x, y)
turtle.done()
