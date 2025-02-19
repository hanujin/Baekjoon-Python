while True:
    n = int(input())
    if n == -1:
        break
    else:
        divisors = [i for i in range(1,n) if n % i == 0]

        if n == sum(divisors):
            print(f'{n} = {' + '.join(map(str, divisors))}')
        else:
            print(f'{n} is NOT perfect.')                