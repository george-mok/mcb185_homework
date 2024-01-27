# 24accuracy.py by George Mo

import math
import sys

"""
Calculates F1 score from true positives (TP), 
false positives (FP), and false negatives (FN)
"""
# F1 score = TP/(TP + 0.5(FP + FN))

def f1(TP, FP, FN):
	assert(TP > 0)
	assert(FP >= 0)
	assert(FN >= 0)
	return (TP)/(TP + 0.5*(FP + FN))

print (F1(3, 2, 1))