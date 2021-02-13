import sys
input = sys.stdin.readline

from collections import deque

V,E = map(int,input().split())
indegree = [0 for _ in range(V+1)]
graph = [[]for _ in range(V+1)]

for _ in range(E):
    start,end = map(int,input().split())
    graph[start].append(end)
    indegree[end] += 1

def topology_sort():
    result = []
    q = deque()

    for i in range(1,V+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    return result

result = topology_sort()
print(result)
