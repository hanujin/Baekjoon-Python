import sys
from collections import Counter

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
checks = list(map(int, sys.stdin.readline().split()))

count = Counter(cards)

for j in range(M):
    if checks[j] in count:
        print(count.get(checks[j]), end = ' ')
    else:
        print(0, end = ' ')