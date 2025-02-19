moneys = [25, 10, 5 , 1]
for _ in range(int(input())):
    s = int(input())
    for i in moneys:
        print(s // i, end=' ')
        s %= i
    print()