import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input())

data =[]


for i in range(1,N+1):
    end, cost = map(int,input().split())
    tmp = [end+i,cost,i]
    heapq.heappush(data,tmp)

def solution(N,data):
    dp = [0 for _ in range(N+2)]
    for i in range(1,N+2):

        while data:
            if data[0][0] == i:
                now = heapq.heappop(data)
                end, cost, start = now[0], now[1], now[2]
                dp[end] = max(dp[start] + cost, dp[end])
            else: break

        dp[i] = max(dp[i-1],dp[i])

    return dp

result = solution(N,data)
print(max(result))