N = int(input())
T = list(map(int, input().split()))

T.sort()
time = [0] * N
time[0] = T[0]

for i in range(N-1):
    time[i+1] = T[i+1] + time[i]

print(sum(time))