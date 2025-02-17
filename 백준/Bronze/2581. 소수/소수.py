import math

M = int(input())
N = int(input())

prime_num = []
for i in range(M, N+1):
    if i < 2:
        continue
    is_prime = True
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j ==0:
            is_prime = False
            break
    if is_prime:
        prime_num.append(i)

 
if prime_num:
    print(sum(prime_num))
    print(min(prime_num))  
else:
    print(-1)   