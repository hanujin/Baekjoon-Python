for _ in range(int(input())):
    H, W, N = map(int, input().split())
    room = 101
    while N > 0:
        if N - H > 0:
            room += 1
            N -= H
        else: 
            room += 100*(N-1)
            N -= H
    print(room)