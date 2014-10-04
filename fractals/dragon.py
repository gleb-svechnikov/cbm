import turtle

def dragon(it, level):
    if level == 0:
        return it
    nit = [not x for x in it]
    nit.reverse()
    it.append(True)
    it += nit
    return dragon(it, level - 1)

def draw_fractal(size, level):
    angleSize = size / 5
    window = turtle.Screen()
    window.bgcolor("yellow")
    mule = turtle.Turtle()
    mule.shape("classic")
    mule.speed(3000)
    frame = dragon([True], level)
    for switch in frame:
        mule.forward(size-angleSize)
        if switch:
            mule.right(90)
            mule.forward(angleSize)
            mule.left(90)
            mule.forward(angleSize)
            mule.right(90)
        else:
            mule.left(90)
            mule.forward(angleSize)
            mule.right(90)
            mule.forward(angleSize)
            mule.left(90)
    window.exitonclick()


draw_fractal(6,10)
