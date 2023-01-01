

from turtle import *	
def shape_flower(j):
	pensize(j)
	forward(5)
	
def draw():
	penup()
	goto(0,0)
	pendown()
	left(36)
color("red")
for i in range(10):
	for j in range(20,60,2):
		shape_flower(j)
	
