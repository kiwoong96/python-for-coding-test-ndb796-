import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
N, M = map(int,input().split())

graph = [[] for _ in range(N+1)]

for i in range(M):
    start, end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)

def solution(graph):
    distance = [INF for _ in range(N+1)]
    q = []
    heapq.heappush(q,(0,1))#dist, start
    distance[1] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for new in graph[now]:
            if distance[new] > dist + 1 :
                distance[new] = dist + 1
                q.append((dist+1 , new))

    return distance

distance = solution(graph)

print(distance.index(max(distance[1:])),max(distance[1:]),distance.count(max(distance[1:])))
