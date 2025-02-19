import sys
input = sys.stdin.readline

N = int(input().strip()) 
A = []

for _ in range(N):
    x, y = map(int, input().split())
    A.append((x, y))

A.sort(key=lambda x: (x[1], x[0])) 

sys.stdout.write("\n".join(f"{x} {y}" for x, y in A) + "\n")