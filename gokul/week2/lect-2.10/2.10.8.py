# simulate a coin toss, if the random number generated is >0.5 , print 'heads' else 'tails'



import random
a = random.random()
print("Random number a:", a)
if a > 0.5:
  print("Heads")
else:
  print("Tails")
