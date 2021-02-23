import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int,input().split()))

dp = [1 for _ in range(N)]

for i in range(1,N):
    for j in range(i):
        if data[i] < data[j]:
            dp[i] = max(dp[i],dp[j]+1)



print(N-max(dp))