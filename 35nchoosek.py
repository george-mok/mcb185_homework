# 35nchoosek.py by George Mo

# Factorial function

def factorial(n):
	if n == 0: return 1
	fact = 1
	for i in range(1, n+1):
		fact = fact * i
	return fact
	
# nchoosek

def nchoosek(n, k):
	comb = (factorial(n)) / ((factorial(k)) * (factorial(n - k)))
	return comb
	
print(nchoosek(3, 1))
print(nchoosek(5, 2))
print(nchoosek(20, 3))
print(nchoosek(20, 7))