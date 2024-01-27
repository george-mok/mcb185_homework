# 24accuracy.py by George Mo

import math
import sys

"""
Calculates accuracy and F1 score from true positives (TP), 
true negatives, (TN) false positives (FP), and false negatives (FN).
"""
# F1 score = TP/(TP + 0.5(FP + FN))
# Output in form: (accuracy, F1 score)

def f1(TP, FP, TN, FN):
	assert(TP >= 0)
	assert(TN >= 0)
	assert(FP >= 0)
	assert(FN >= 0)
	acc = (TP + TN)/(TP + FP + TN + FN)
	f = (TP)/(TP + 0.5*(FP + FN))
	return (acc, f)

print(f1(3, 2, 1, 0))
print(f1(8, 3, 4, 2))
print(f1(3, 0, 2, 0))
print(f1(0, 0, 0, 0))