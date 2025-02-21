from collections import deque

def dfs(net, visited, start):
    visited[start] = True
    print(start, end = " ")

    for node in net[start]:
        if not visited[node]:
            dfs(net, visited, node)

def bfs(net, visited, start):
    visited[start] = True
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node, end = " ")

        for neighbor in net[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

N, M, V = map(int, input().split())

net = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    net[a].append(b)
    net[b].append(a)

for i in range(1, N+1):
    net[i].sort()


visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)

dfs(net, visited_dfs, V)
print()
bfs(net, visited_bfs, V)