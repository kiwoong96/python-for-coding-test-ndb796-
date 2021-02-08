import sys
input = sys.stdin.readline
INF = int(1e9)

V = int(input())
E = int(input())

board = [[INF for _ in range(V+1)] for _ in range(V+1)]

for i in range(E):
    start,end,dist = map(int,input().split())
    board[start][end] = dist

for i in range(1,V+1):
    for j in range(1,V+1):
        if i == j: board[i][j] = 0
        else:
            for k in range(1,V+1):
                board[i][j] = min(board[i][j],board[i][k] + board[k][j])



for i in range(1,V+1):
    for j in range(1,V+1):
        if board[i][j]== INF:
            print("INF",end = ' ')
        else:
            print(board[i][j], end = ' ')
    print()

