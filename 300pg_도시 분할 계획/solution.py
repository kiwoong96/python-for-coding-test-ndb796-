import sys
input = sys.stdin.readline

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b



N,M = map(int,input().split())

edges = []
parent = [i for i in range(N+1)]
for _ in range(M):
    a,b,cost = map(int,input().split())
    edges.append((a,b,cost))


edges.sort(key = lambda x:x[2])
result = 0
max = -1
for i in range(M):
    a,b,cost = edges[i][0],edges[i][1],edges[i][2]
    if find_parent(parent,a) == find_parent(parent,b):
        continue
    else:
        union_parent(parent,a,b)
        result += cost
        max = cost

print(result - max)

