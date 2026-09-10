# find the difference between

import math

print(math.pow(10,0.5))
print(10**0.5)

# why to use math.pow and 10**0.5
they both are same and gave the same output. 

#  is there any difference in speed between pow and 10**0.5
Yes, in Python, the infix operator 10**0.5 is significantly faster than calling the function pow(10, 0.5) because pow() requires an extra function call overhead

# check this out : https://stackoverflow.com/questions/20969773/exponentials-in-python-xy-vs-math-powx-y
