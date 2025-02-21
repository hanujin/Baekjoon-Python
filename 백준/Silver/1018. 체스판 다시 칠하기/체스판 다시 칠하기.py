N, M = map(int, input().split())
board = []
count = []

for _ in range(N):
    board.append(input())

for a in range(N-7):
    for b in range(M-7):
        black = 0
        white = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if board[i][j] != 'B':
                        black += 1
                    if board[i][j] != 'W':
                        white += 1
                else:
                    if board[i][j] != 'W':
                        black += 1
                    if board[i][j] != 'B':
                        white += 1                        
        count.append(black)
        count.append(white)
print(min(count))     