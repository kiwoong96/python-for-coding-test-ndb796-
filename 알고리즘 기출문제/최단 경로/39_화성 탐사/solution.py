import sys
input = sys.stdin.readline
INF = int(1e9)
T = int(input())

for _ in range(T):
    N = int(input())

    board = []
    for _ in range(N):
        board.append(list(map(int,input().split())))


    dp = [[INF for _ in range(N+2)]for _ in range(N+2)]

    for i in range(1,N+1):
        for j in range(1,N+1):
            dp[i][j] = board[i-1][j-1]

    for i in range(1,N+1):
        for j in range(1,N+1):
            if i == 1 and j == 1: continue
            dp[i][j] = min(dp[i-1][j] + dp[i][j], dp[i][j-1] + dp[i][j])

    for i in dp:
        print(i)

