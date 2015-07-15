# -*- coding: utf-8 -*-

import sympy
from sympy import *
import math

'''
-log(-x)/log(5) + log(x**2 - 12)/log(5)
-log(x)/log(10) + log((x + 8)/(x - 1))/log(10)
'''

'''
Функция принимает символьное представления выражения, 
решает уравнение выражение = 0 
	- не ловит исключения
'''
def SolveStringEquation ( stringExpression ):
	expression = sympify ( stringExpression )
	equation = Eq(expression, 0)

	x = symbols('x')
	solution = solve ( equation, x )

	return solution

equation1 = "-log(-x)/log(5) + log(x**2 - 12)/log(5)"
solution1 = SolveStringEquation(equation1)
print solution1

equation2 = "-log(x)/log(10) + log((x + 8)/(x - 1))/log(10)"
solution2 = SolveStringEquation(equation2)
print solution2

#x1,x2 = solution2[0], solution2[1]
#a = -math.log(-x1)/math.log(5) + math.log(x1**2 - 12)/math.log(5)
#b = -math.log(-x2)/math.log(5) + math.log(x2**2 - 12)/math.log(5)
#print a, b

'''
-log(-x)/log(5) + log(x**2 - 12)/log(5)
-log(x)/log(10) + log((x + 8)/(x - 1))/log(10)
'''

