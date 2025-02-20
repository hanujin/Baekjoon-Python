from collections import deque

n = int(input())
stack = deque()
target = 1
result = []

for i in range(n):
    num = int(input())
    while target <= num:
        stack.append(target)
        result.append("+")
        target += 1

    if stack and stack[-1] == num:
        result.append("-")
        stack.pop()
    else:
        print("NO")
        exit() 
print("\n".join(result))