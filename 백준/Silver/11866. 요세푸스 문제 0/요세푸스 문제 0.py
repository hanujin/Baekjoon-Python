from collections import deque

N, K = map(int, input().split())
people = deque(range(1, N+1))
result = []

while people:
    for _ in range(K-1):
        people.append(people.popleft())
    result.append(people.popleft())

print(str(result).replace('[', '<').replace(']', '>'))