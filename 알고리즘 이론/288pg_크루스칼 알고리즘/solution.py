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


V,E = map(int,input().split())
parent = [i for i in range(V+1)]
list = []
for i in range(E):
    start,end,cost = map(int,input().split())
    list.append((start,end,cost))

list.sort(key = lambda x:x[2])

result = 0
for i in range(E):
    a,b,cost = list[i][0],list[i][1], list[i][2]
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a==b:
        continue
    else:
        union_parent(parent,a,b)
        result += cost
print(result)