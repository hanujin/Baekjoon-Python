N, K = map(int, input().split())
money = [int(input()) for _ in range(N)]

money.sort(reverse=True)
count = 0

for i in money:
    count += K//i
    K %= i
        
print(count)