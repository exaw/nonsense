# -*- coding: utf-8 -*-

import sympy
from sympy import *
import math
from sympy.utilities.solution import *
from sympy.utilities.solution_log import log_as_latex, log_to_file

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

x = symbols('x')
#expression = 4*x**2 - 3*x + 3
#equation = Eq(expression, 0)
#solution = solve ( equation, x )


#limit(sin(x)/x, x, 0)
#expr = Limit((cos(x) - 1)/x, x, 0)
#expr.doit()

init_printing()

equation1 = "-log(-x)/log(5) + log(x**2 - 12)/log(5)"
solution1 = SolveStringEquation(equation1)
print solution1
log_to_file('report_1.tex', log_as_latex(last_solution()))

reset_solution()

equation2 = "-log(x)/log(10) + log((x + 8)/(x - 1))/log(10)"
solution2 = SolveStringEquation(equation2)
print solution2
log_to_file('report_2.tex', log_as_latex(last_solution()))

#pprint (Integral (sqrt(1/x),x), use_unicode=False)
#pprint (sol)


# dir (sol)
# print sol


#print expr

#print solution



# print solution1

# equation2 = "-log(x)/log(10) + log((x + 8)/(x - 1))/log(10)"
# solution2 = SolveStringEquation(equation2)
# print solution2

#x1,x2 = solution2[0], solution2[1]
#a = -math.log(-x1)/math.log(5) + math.log(x1**2 - 12)/math.log(5)
#b = -math.log(-x2)/math.log(5) + math.log(x2**2 - 12)/math.log(5)
#print a, b

'''
-log(-x)/log(5) + log(x**2 - 12)/log(5)
-log(x)/log(10) + log((x + 8)/(x - 1))/log(10)
'''

