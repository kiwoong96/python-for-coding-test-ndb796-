import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)

N,M,C = map(int,input().split())

graph = [[] for _ in range(N+1)]

distance = [INF for _ in range(N+1)]

for i in range(M):
    start, end, dist = map(int,input().split())
    graph[start].append((end,dist))

#C = start

def dijkstar(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        tmp = heapq.heappop(q)
        dist, now = tmp[0], tmp[1]
        ##기억!!
        if distance[now] < dist:
            continue
        for i in graph[now]:
            end, dist = i[0], i[1]
            data = distance[now] + dist
            if distance[end] > data:
                distance[end] = data
                heapq.heappush(q,(data,end))



dijkstar(C)

print(distance)
country = 0
max = -1
for i in range(1,N+1):
    if distance[i] != INF and distance[i] != 0:
        country +=1
        if max < distance[i]:
            max = distance[i]

print(country,max)
