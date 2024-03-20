# 65transmembrane.py by George Mo and Khalid Saif

import sys
import mcb185
import dogma

path = sys.argv[1]

def avg_kd(seq, w):
	total_kd = []
	for i in range(len(seq) -w +1):
		window = seq[i:i+w]
		kd_sum = 0
		for aa in window:
			kd_sum += dogma.kdhydro(aa)
		total_kd.append(kd_sum / w)
	return total_kd

"""check for signal and transmembrane region 
aa length (w), position, and hydro value as variables"""

def hydro_reg(seq, w, threshold):
	kd_list = avg_kd(seq, w)
	for i, kd in enumerate(kd_list):
		if kd >= threshold and 'P' not in seq[i:i+w]:
			return True
		else:
			False
			
for defline, seq in mcb185.read_fasta(path):
	signal = hydro_reg(seq[:30], 8, 2.5)
	trans_reg = hydro_reg(seq[30:], 11, 2.0)
	if signal == True and trans_reg == True:
		print(defline)