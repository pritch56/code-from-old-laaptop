import random
die1 = random.randint(1,6)
die2 = random.randint(1,6)
score = die1 + die2
if die1 == die2:
	score = score * 2
print(score)

