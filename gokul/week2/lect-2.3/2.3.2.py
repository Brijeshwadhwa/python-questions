# 1. what is dynamic typing?




Python determines a variable's data type automatically at runtime, rather than requiring you to declare it explicitly beforehand.


example :
# Python automatically infers that x is an integer
x = 42			
print(type(x))  # Output: <class 'int'>

# Reassigning the same variable to a string works perfectly
x = "Hello, Python!"	
print(type(x))  # Output: <class 'str'>
