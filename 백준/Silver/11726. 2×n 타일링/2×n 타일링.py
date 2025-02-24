n = int(input())
list = [0] * n
list[0] = 1

if n >= 2:
    list[1] = 2
    for i in range(2, n):
        list[i] = list[i-1] + list[i-2]

print(list[n-1]%10007)