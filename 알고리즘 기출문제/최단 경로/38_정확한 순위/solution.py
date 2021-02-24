import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int,input().split())

graph = [[INF for _ in range(N+1)]for _ in range(N+1)]

for i in range(M):
    start, end = map(int,input().split())
    graph[start][end] = 1

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i == j: graph[i][j] = 0
            else:
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]


answer = 0
for i in range(1,N+1):
    now = i
    result = 0
    for j in range(1,N+1):
        if graph[now][j] == INF and graph[j][now] == INF:
            break
        else:
            result +=1

    if result == N:
        answer += 1

print(answer)