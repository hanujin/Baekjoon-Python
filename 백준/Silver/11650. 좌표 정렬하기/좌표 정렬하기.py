import sys

N = int(sys.stdin.readline().strip()) 
A = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    A.append((x, y))

A.sort(key=lambda x: (x[0], x[1])) 

sys.stdout.write("\n".join(f"{x} {y}" for x, y in A) + "\n")