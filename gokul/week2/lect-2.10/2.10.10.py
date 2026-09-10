# look at the below code
import random
print(random.randrange(1,6))

# will 6 get printed in the console or not?

No, 6 will not get printed in the console.
random.randrange(start, stop) function in Python includes the start integer but excludes the stop integer. 
Therefore, random.randrange(1, 6) will only generate numbers from the set {1, 2, 3, 4, 5}.
If you want to include the number 6, you can use either of these alternatives:
random.randrange(1, 7)random.randint(1, 6) (The randint function does include the upper limit)
