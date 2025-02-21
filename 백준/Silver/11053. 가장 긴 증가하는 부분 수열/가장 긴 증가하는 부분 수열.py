N = int(input())
A = list(map(int, input().split()))
length = [1] * N

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            length[i] = max(length[i], length[j] + 1)

print(max(length))