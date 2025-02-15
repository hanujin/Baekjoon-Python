N = int(input())
A = []

for _ in range(N):
    A.append(input())

A = list(set(A))

A.sort(key=lambda x: (len(x), x))
print(*A, sep="\n")