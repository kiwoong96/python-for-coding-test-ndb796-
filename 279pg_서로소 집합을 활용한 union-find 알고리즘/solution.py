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


v,e = map(int,input().split())
parent = [i for i in range(v+1)]
for i in range(e):
    a,b = map(int,input().split())
    union_parent(parent,a,b)

for i in range(1,v+1):
    print(find_parent(parent,i), end=' ')

print()

for i in parent:
    print(i,end = ' ')