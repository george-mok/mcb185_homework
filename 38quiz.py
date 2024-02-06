# 38quiz.py by George M., Jordan S., Khalid S. Ethan D.

# Task 1


def gregory(n):
	denom = 3
	pi = 4
	for i in range(n):
		calc = 4 / denom
		if i % 2 == 0:
			calc = -1 * calc
		else:
			calc = calc
		pi = pi + calc
		denom = denom + 2
	return pi

print(gregory(100))