import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int,input().split())
start = int(input())

graph = [[] for _ in range(N+1)]

visited = [False for _ in range(N+1)]

distance = [INF for _ in range(N+1)]

for i in range(M):
    tmp = list(map(int,input().split()))
    graph[tmp[0]].append((tmp[1],tmp[2]))

def get_smallest_node():
    min_value = INF
    idx = 0
    for i in range(1,N+1):
        if visited[i] == False:
            if min_value > distance[i]:
                min_value = distance[i]
                idx = i

    return idx

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for i in graph[start]:
        distance[i[0]] = i[1]

    print(distance)
    for i in range(N-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now]+j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
        print(distance)

dijkstra(start)
