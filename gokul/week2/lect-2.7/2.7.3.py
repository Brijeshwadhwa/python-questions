# predict the output


alpha="abcdefghijklmnopqrstuvwxyz"
i=24

print(alpha[i+1])
print(alpha[i+2])
print(alpha[i+2]%26)
print(alpha[(i+2)%26])


output:


z

Traceback (most recent call last):
  File "<main.py>", line 8, in <module>
IndexError: string index out of range

Traceback (most recent call last):
  File "<main.py>", line 9, in <module>
IndexError: string index out of range

a
