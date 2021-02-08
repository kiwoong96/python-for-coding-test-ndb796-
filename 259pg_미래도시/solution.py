import sys
INF = int(1e9)

input = sys.stdin.readline


N, M = map(int,input().split())

board = [[INF for _ in range(N+1)] for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        if i==j: board[i][j] = 0

for i in range(M):
    start, end = map(int,input().split())
    board[start][end] = 1
    board[end][start]= 1

X,K = map(int,input().split())

for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):
            board[i][j] = min(board[i][j], board[i][k] + board[k][j] )

for i in range(1,N+1):
    for j in range(1,N+1):
        print(board[i][j], end= '\t')
    print()
if board[1][K] + board[K][X] < INF:
    print(board[1][K] + board[K][X])
else:
    print(-1)