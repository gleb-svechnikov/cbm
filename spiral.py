from turtle import *
from math import *
def spiral(a, b):
	for i in range(0, 1000):
		t = radians(i)
		x = (a+b*t)*cos(t)
		y = (a+b*t)*sin(t)
		setpos(x, y)
spiral(0.5, 5)
