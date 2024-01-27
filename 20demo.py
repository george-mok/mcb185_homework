# 20demo.py by George Mo

import math
import sys

print ('hello, again') # greeting
print (19 // 2)
print (19 % 2)
print (math.floor(7.2))
print (abs(-89))
print (0.1 * 3)

#a = 3                       # side of triangle
#b = 4                       # side of triangle
#c = math.sqrt(a**2 + b**2)  # hypotenuse
#print(c)

def pythagoras(a, b):
    if a <= 0: sys.exit('error: a must be greater than 0')
    if b <= 0: sys.exit('error: b must be greater than 0')
    return math.sqrt(a**2 + b**2)
print(pythagoras(3,4))

#def signchange(a):
    #return (a * -1)
#print (signchange(-6))

#def midpoint(x1, y1, x2, y2):
    #return ((x1 + x2)/2), ((y1 + y2)/2)
#print (midpoint(3, 4, 6, 10))

#s = 'hello world'
#print(s, type(s))

a = 2
b = 2
if a == b:
    print ('a equals b')
#print (a,b)

c = a == b
print(c)
print(type(c))

if      a < b or a > b: print('all things being equal, a and b are not')
#if      a < b: print('a > b')
if not False:           print (True)

#def is_integer(a)
    #if abs(a)