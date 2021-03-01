import sys
input = sys.stdin.readline

G = int(input())
P = int(input())


def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def solution(G,P):
    parent = [i for i in range(G+1)]
    result = 0
    for _ in range(P):
        data = int(input())
        now = find_parent(parent,data)
        if now == 0:
            break
        else:
            result+=1
            union(parent,now,now-1)

    return result

result = solution(G,P)

print(result)