from functools import *

def multiplier(x, y):
	return x * y

double = partial(multiplier, y = 2)
triple = partial(multiplier, y = 3)

print('Double of 5 is {}'.format(double(5)))
# Double of 5 is 10

print('Triple of 5 is {}'.format(triple(5)))
# Triple of 5 is 15

print('Function powering double is {}'.format(double.func))
# Function powering double is <function multiplier at 0x7fd0395297d0>

print('Default keyword of double is {}'.format(double.keywords))
# Default keyword of double is {'y': 2}

print("Vishal")
