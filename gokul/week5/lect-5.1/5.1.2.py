# create a function named `sub` that takes three parameters as input and  returns their the minimum difference among the three

def sub(a,b,c):
  return min(abs(a, b), abs(b, c), abs(c, a))

assert sub(1,2,3) == 1
assert sub(2,3,4) == 1
assert sub(3,4,5) == 1
