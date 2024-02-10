# 44randompi.py by George Mo

import random

inside = 0
total = 0
while True:
	x = random.random()
	y = random.random()
	dist = (x**2 + y**2)**2
	if dist < 1:
		inside += 1
		total += 1
	else:
		total += 1
	print(4*(inside/total))