import sys
input = sys.stdin.readline

def find_parents(parent,x):
    if parent[x] != x:
        parent[x] = find_parents(parent,parent[x])
    return parent[x]

def union_parents(parent,a,b):
    a = find_parents(parent,a)
    b = find_parents(parent,b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b

v,e = map(int,input().split())
parent = [i for i in range(v+1)]

cycle = False

for i in range(e):
    a,b = map(int,input().split())
    if find_parents(parent,a) == find_parents(parent,b):
        cycle = True
        break
    else:
        union_parents(parent,a,b)

if cycle:
    print("사이클 발생")
else:
    print("사이클 발생하지 않음.")