# print True if the input string starts with I and ends with N

x=input()




my solution:


print("Write a string: ")
x = input()

# Fixed: Added quotes around "I" and "N", and changed 'or' to 'and'
if x[0] == "I" and x[-1] == "N":
    print("True")
else:
    print("False")


GEMINI SOLUTION:

x = input()
print(x.startswith("I") and x.endswith("N"))
