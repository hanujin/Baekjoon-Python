import sys

input = sys.stdin.readline
s = set()

for _ in range(int(input())):
    command = input().split()

    if command[0] == "add":
        s.add(int(command[1]))
    elif command[0] == "remove":
        s.discard(int(command[1]))
    elif command[0] == "check":
        print(1 if int(command[1]) in s else 0)
    elif command[0] == "toggle":
        s.discard(int(command[1]) if int(command[1]) in s else s.add(int(command[1])))
    elif command[0] == "all":
        s = set(range(1, 21))
    elif command[0] == "empty":
        s = set()