from turtle import *

def koch(length, depth):
   if depth == 0:
     forward(length)
   else:
     koch(length/3, depth-1)
     right(60)
     koch(length/3, depth-1)
     left(120)
     koch(length/3, depth-1)
     right(60)
     koch(length/3, depth-1)

koch(500, 4)
