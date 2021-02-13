from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

graph = [[]for _ in range(N+1)]
cost = [0 for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
for i in range(1,N+1):
    tmp = list(map(int,input().split()))
    cost[i] = tmp[0]
    for j in range(1,N):
        if tmp[j] == -1:
            break
        else:
            graph[tmp[j]].append(i)
            indegree[i] += 1

def topology():
    result = []
    q = deque()

    for i in range(1,N+1):
        if indegree[i] == 0:
            q.append((i,cost[i]))

    while q:
        now = q.popleft()
        V, Vcost = now[0], now[1]
        result.append(Vcost)
        for j in graph[V]:
            indegree[j] -= 1
            now_VCost = Vcost + cost[j]
            if indegree[j]==0:
                q.append((j,now_VCost))
    return result

result = topology()

for x in result:
    print(x)




"""
data = [10,1,2,3,-1]

for x in data[1:-1]:
    print(x)
"""


