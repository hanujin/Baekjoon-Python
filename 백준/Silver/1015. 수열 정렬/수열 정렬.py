N = int(input())
A = list(map(int, input().split()))
sortA = sorted(A, reverse=False)

P = []
for i in range(N):
    P.append(sortA.index(A[i]))
    sortA[sortA.index(A[i])] = -1
    
print(*P)