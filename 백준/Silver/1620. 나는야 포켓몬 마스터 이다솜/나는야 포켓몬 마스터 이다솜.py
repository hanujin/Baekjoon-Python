import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dogam_int = {}
dogam_name = {}

for i in range(N):
    name = input().strip()
    dogam_int[i] = name
    dogam_name[name] = i

for _ in range(M):
    q = input().strip()
    if q.isdigit():
        print(dogam_int[int(q)-1])
    else:
        print(dogam_name[q]+1)