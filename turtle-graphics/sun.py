from turtle import *

color('red', 'yellow')
speed(1)
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
