import sys
input = sys.stdin.readline
INF = int(1e9)

T = int(input())


def solution(board):
    dp = [[0 for _ in range(M+1)] for _ in range(N+2)]
    for j in range(1,M+1):
        for i in range(1,N+1):
            dp[i][j] = max(dp[i][j-1],dp[i-1][j-1],dp[i+1][j-1]) + board[i-1][j-1]

    result = 0
    for i in range(1,N+1):
        if result < dp[i][M]:
            result = dp[i][M]
    return result

for _ in range(T):
    board = []
    N,M = map(int,input().split())
    data = list(map(int,input().split()))

    for i in range(N):
        board.append(data[i*M:(i+1)*M])

    result = solution(board)
    print(result)
