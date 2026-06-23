# 1) generate the following pattern using print statements
#     ```
#     *
#     **
#     ***
#     ****
#     *******
#     *********#
#     i don't know what to type
#     ```

# number of rows
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")
