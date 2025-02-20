switch_num = int(input())
switch = [-1] + list(map(int, input().split()))

for _ in range(int(input())):
    gender, num = map(int, input().split())
    if gender == 1:
        for i in range(num, switch_num+1, num):
            switch[i] = 1 - switch[i]
    else:
        switch[num] = 1 - switch[num]

        for k in range(switch_num//2):
            if num + k > switch_num or num - k < 1: break
            if switch[num + k] == switch[num - k]:
                switch[num + k] = 1 - switch[num + k]
                switch[num - k] = 1 - switch[num - k]
            else:
                break
                
for i in range(1, switch_num+1):
    print(switch[i], end = " ")
    if i % 20 == 0 :
        print()