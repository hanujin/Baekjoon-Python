from itertools import combinations

N, M = map(int, input().split())
A = list(map(int, input().split()))

result = 0

for i in combinations(A, 3):
    sum_value = sum(i)
    if sum_value <= M:
        result = max(sum_value, result) 

print(result)