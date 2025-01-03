import sys

input = sys.stdin.read
data = input().split()

N = int(data[0]) 
A = list(map(int, data[1:]))

for num in sorted(A):
    print(num)