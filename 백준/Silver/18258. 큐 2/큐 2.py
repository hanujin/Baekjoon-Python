import sys
from collections import deque

input = sys.stdin.readline
q = deque()

for _ in range(int(input())):
    command = input().split()

    if command[0] == "push":
        q.append(int(command[1]))
    elif command[0] == "pop":
        print(q.popleft() if q else -1)
    elif command[0] == "size":
        print(len(q))
    elif command[0] == "empty":
        print(1 if not q else 0)
    elif command[0] == "front":
        print(q[0] if q else -1)
    elif command[0] == "back":
        print(q[-1] if q else -1) 