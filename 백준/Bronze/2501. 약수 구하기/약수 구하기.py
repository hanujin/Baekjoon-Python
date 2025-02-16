N, K = map(int, input().split())
divisor = []
for i in range(1, N+1):
    if N%i == 0:
        divisor.append(i)

divisor = sorted(divisor)
print(divisor[K-1] if K <= len(divisor) else 0)