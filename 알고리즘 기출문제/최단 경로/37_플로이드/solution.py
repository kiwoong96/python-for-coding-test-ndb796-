import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
M = int(input())
graph = [[INF for _ in range(N+1)] for _ in range(N+1)]

for i in range(M):
    start,end,distance = map(int,input().split())
    graph[start][end] = min(graph[start][end],distance)

def solution(graph):
    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                if i == j:
                    graph[i][j] = 0
                else:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


    return graph

graph = solution(graph)
for i in range(1,N+1):
    for j in range(1,N+1):
        if graph[i][j] != INF:
            print(graph[i][j], end = ' ')
        else:
            print(0, end= ' ')
    print()




