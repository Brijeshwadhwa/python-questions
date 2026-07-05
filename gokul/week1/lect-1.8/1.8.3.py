# 1. what will be the value stored in each variable?
#     ```
#     a=int(5.7)
#     b=int('10')
#     c=int("212")
#     d=float("1.2")
#     e=int("1.2")
#     ```





a = 5: The int() function truncates the float 5.7 down to the whole number 5.
b = 10: The string '10' is successfully converted into the integer 10.
c = 212: The string "212" is successfully converted into the integer 212.
d = 1.2: The string "1.2" is successfully evaluated and stored as the float 1.2.
e: This will throw a ValueError because "1.2" is not a valid integer string. 
  You cannot directly pass a string with a decimal point into int(); 
    it would first need to be converted to a float().
