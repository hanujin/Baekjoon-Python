import sys
from collections import deque

input = sys.stdin.readline
stack = deque()

for _ in range(int(input())):
    command = input().split()

    if command[0] == "1":
        stack.append(command[1])
    elif command[0] == "2":
        print(stack.pop() if stack else -1)
    elif command[0] == "3":
        print(len(stack))
    elif command[0] == "4":
        print(1 if not stack else 0)
    elif command[0] == "5":
        print(stack[-1] if stack else -1) 