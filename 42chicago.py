# 42chicago.py by George Mo

import random
import sys

totalscore = 0
zerogames = 0
gamesplayed = 1000000
log = gamesplayed // 100 # reports progress a 1% intervals
for i in range(gamesplayed):
	if i % log == 0: print(f'{100 * i/gamesplayed:.0f}', file=sys.stderr)
	score = 0
	for roundnumber in range(2, 13):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1 + d2 == roundnumber:
			score += roundnumber
	if score == 0:
		zerogames += 1
	totalscore += score		
print(zerogames / gamesplayed)
print(totalscore / gamesplayed)