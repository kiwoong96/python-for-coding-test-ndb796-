import sys
input = sys.stdin.readline
INF = int(1e9)
N, M = map(int,input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))


to_visit = list(map(int,input().split()))
parent = [i for i in range(N+1)]

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a<b :
        parent[b] = a
    else:
        parent[a] = b


def solution(graph):

    for i in range(N):
        for j in range(i,N):
            if graph[i][j] == 1:
                a = find_parent(i+1)
                b = find_parent(j+1)
                if a==b:
                    continue
                else:
                    union(a,b)
solution(graph)

parentno = find_parent(to_visit[0])


result = True
for k in to_visit[1:]:
    if find_parent(k) != parentno:
        result = False
        break


if result == False:
    print("NO")
else:
    print("YES")