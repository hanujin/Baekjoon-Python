import sys
from collections import Counter

input = sys.stdin.readline

arr = []
for _ in range(int(input())):
    arr.append(int(input()))

print(round(sum(arr)/len(arr)))

arr.sort()
print(arr[len(arr)//2])

counter = Counter(arr)
most_common = counter.most_common()

if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
    print(most_common[1][0])
else:
    print(most_common[0][0])   

print(max(arr) - min(arr))