# 21quadratic.py by George Mo

import math
import sys

# Solves real roots for quadratic formula: ax^2 + bx + c

def quadratic(a, b, c):
	if b**2 - 4*a*c < 0:
		return 'None, None'
	if b**2 - 4*a*c == 0:
		x = (((-1)*b) + math.sqrt((b**2) - 4*a*c)/(2*a))
		return x, x
	if b**2 - 4*a*c > 0:
		x1 = (((-1)*b) - math.sqrt((b**2) - 4*a*c)/(2*a))
		x2 = (((-1)*b) + math.sqrt((b**2) - 4*a*c)/(2*a))
		return (x1, x2)

print(quadratic(3, 4, 0)) # two real solutions
print(quadratic(2, 8, 2)) # two real solutions
print(quadratic(8, 2, 2)) # no solutions
print(quadratic(4, 4, 1)) # one real solution
print(quadratic(-3, 4, 5)) # two real solutions