import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int,input().split())
start = int(input())

graph = [[] for _ in range(N+1)]

distance = [INF for _ in range(N+1)]

for i in range(M):
    tmp = list(map(int,input().split()))
    graph[tmp[0]].append((tmp[1],tmp[2]))


def dijkstra(start):
    q = []

    heapq.heappush(q, (0,start))
    distance[start] = 0

    while q:
        tmp = heapq.heappop(q)
        dist, now = tmp[0], tmp[1]
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist+i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)