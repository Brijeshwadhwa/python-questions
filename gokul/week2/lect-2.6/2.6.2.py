x=input()

# print true is all characters are lower case
# print True if all the characters are upper case
# print True if the string follows the rules of title (all the words have starting letter in capital)




output:

x = input()

# Check if all characters are lowercase
if x.islower():
    print(True)

# Check if all characters are uppercase
elif x.isupper():
    print(True)

# Check if the string follows title case rules
elif x.istitle():
    print(True)
