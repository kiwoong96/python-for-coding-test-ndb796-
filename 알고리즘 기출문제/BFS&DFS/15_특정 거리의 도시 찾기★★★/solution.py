from _collections import deque
import sys
input = sys.stdin.readline



INF = int(1e9)
##다익스트라 알고리즘
N,M,K,X = map(int,input().split())

graph = [[]for _ in range(N+1)]

visited = [False for _ in range(N+1)]

for i in range(M):
    a,b, = map(int,input().split())
    graph[a].append(b)

def BFS(start):
    q = deque()
    result = []
    q.append((0,start))
    visited[start] = True

    while q:
        dist, now = q.popleft()
        if dist == K:
            result.append(now)

        elif dist< K:
            for k in graph[now]:
                if visited[k]== False:
                    q.append((dist+1,k))
                    visited[k] = True
        else:
            break

    return result

result = BFS(X)
result.sort()
if result:
    for i in result:
        print(i)
else:
    print(-1)





"""
4 4 2 1
1 2
1 3
2 3
2 4
"""

