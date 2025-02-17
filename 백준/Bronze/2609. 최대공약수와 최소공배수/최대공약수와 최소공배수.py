a, b = map(int, input().split())

divisor_a = set()
for i in range(1, a+1):
    if a % i ==0:
        divisor_a.add(i)

divisor_b = set()
for i in range(1, b+1):
    if b % i ==0:
        divisor_b.add(i)

divisor = max(divisor_a & divisor_b)
multiple = (a // divisor) * (b // divisor) * divisor

print(divisor)
print(multiple)