from collections import deque
N = int(input())
M = int(input())

net = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    net[a].append(b)
    net[b].append(a)

count = 0
visited = [False] * ((N+1))
def dfs(x):
    global count
    visited[x] = True
    for i in net[x]:
        if not visited[i]:
            count += 1
            dfs(i)

dfs(1)
print(count)