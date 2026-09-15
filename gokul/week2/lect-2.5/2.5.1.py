# predict the output, and use escape characters to parse/fix the output

# print('it's a beautiful day') 
# print("we are from "IIT Madras" Madras")




first i run simple as it is 

ERROR!
Traceback (most recent call last):
  File "<main.py>", line 2
    print('it's a beautiful day') 
                               ^
SyntaxError: unterminated string literal (detected at line 2)



ESCAPE CHARATERS : To fix the errors, you must use the backslash (\) as an escape character right before the inner quotation marks so Python reads them as text rather than code syntax.

after fixing with escapce characters : 


# Fixed using escape characters
print('it\'s a beautiful day') 
print("we are from \"IIT Madras\" Madras")


output : 

it's a beautiful day
we are from "IIT Madras" Madras
