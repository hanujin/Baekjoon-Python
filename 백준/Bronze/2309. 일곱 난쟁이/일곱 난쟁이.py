from itertools import combinations

height = []
for _ in range(9):
    height.append(int(input()))

seven = combinations(height, 7)

for i in list(seven):
    if sum(i) == 100:
        height = i

for i in sorted(height):
    print(i)