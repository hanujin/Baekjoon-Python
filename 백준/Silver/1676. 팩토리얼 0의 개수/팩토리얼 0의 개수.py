import math
num = str(math.factorial(int(input())))
count = 0
for i in num[::-1]:
    if i == "0":
        count += 1
    else:
        break
print(count)