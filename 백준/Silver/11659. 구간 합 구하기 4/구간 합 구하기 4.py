import sys

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

prefix_sum = [0]*(N+1)
for i in range(1, N+1):
    prefix_sum[i] = prefix_sum[i-1] + num[i-1]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(prefix_sum[j] - prefix_sum[i-1])