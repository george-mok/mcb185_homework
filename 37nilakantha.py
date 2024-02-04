# 37nilakantha.py by George Mo

# returns Nilakantha approx. of pi to the nth value of the series

def nilakantha(n):
	denom1 = 2
	denom2 = 3
	denom3 = 4
	pi = 3
	for i in range(n):
		pos = 4 / (denom1 * denom2 * denom3)
		neg = -4 / ((denom1) * (denom2) * (denom3))
		if i % 2 == 0: 
			calc = pos
		else:
			calc = neg
		pi = pi + calc
		denom1 = denom1 + 2
		denom2 = denom2 + 2
		denom3 = denom3 + 2
	return pi
print(nilakantha(16))