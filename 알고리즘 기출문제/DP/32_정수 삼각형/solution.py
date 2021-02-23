import sys
input = sys.stdin.readline


N = int(input())

dp = []

for i in range(N):
    dp.append(list(map(int,input().split())))

def solution(dp):

    for i in range(N-2,-1,-1):
        for j in range(0,i+1):
            dp[i][j] = max(dp[i+1][j],dp[i+1][j+1]) + dp[i][j]

    return dp[0][0]


result = solution(dp)
print(result)