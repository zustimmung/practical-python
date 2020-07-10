# bounce.py
#
# Exercise 1.5
height = 100
factor = 3/5

bounce = 0
while bounce<10:
	bounce = bounce+1
	height = height * factor
	print(bounce, '\t', round(height,4), 'm')
	
