import sympy
from sympy import *
import math

def task1 ():
	x = symbols('x')
	expression = -log(x)/log(10) + log((x + 8)/(x - 1))/log(10)
	equation = Eq(expression, 0)
	solution = solve ( equation, x )
	return solution

def task2 ():
	x = symbols('x')
	expression = -log(-x)/log(5) + log(x**2 - 12)/log(5)
	equation = Eq(expression, 0)
	solution = solve ( equation, x )
	return solution

solution1 = task1()
print solution1

#x1,x2 = solution1[0], solution1[1]
#a = -math.log(x1)/math.log(10) + math.log((x1 + 8)/(x1 - 1))/math.log(10)
#b = -math.log(x2)/math.log(10) + math.log((x2 + 8)/(x2 - 1))/math.log(10)
#print a, b

solution2 = task2()
print solution2

#x1,x2 = solution2[0], solution2[1]
#a = -math.log(-x1)/math.log(5) + math.log(x1**2 - 12)/math.log(5)
#b = -math.log(-x2)/math.log(5) + math.log(x2**2 - 12)/math.log(5)
#print a, b

'''
-log(-x)/log(5) + log(x**2 - 12)/log(5)
-log(x)/log(10) + log((x + 8)/(x - 1))/log(10)
'''

