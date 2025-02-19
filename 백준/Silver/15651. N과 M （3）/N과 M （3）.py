from itertools import product

N, M = map(int,input().split())
num = []

for i in range(1, N+1):
    num.append(i)

for i in product(num, repeat=M):
    print(*i)