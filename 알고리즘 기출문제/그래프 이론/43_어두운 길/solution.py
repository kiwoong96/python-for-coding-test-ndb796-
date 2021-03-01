import heapq
import sys
input = sys.stdin.readline

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

N, M = map(int,input().split())

Edge = []
total_price = 0
for i in range(M):
    x,y,z = map(int,input().split())
    total_price += z
    heapq.heappush(Edge, (z,x,y))

def solution(Edge):
    parent = [i for i in range(N+1)]
    result = 0
    while Edge:
        now = heapq.heappop(Edge)
        dist , a , b = now[0], now[1] , now[2]
        x = find_parent(parent,a)
        y = find_parent(parent,b)
        if x != y:
            result += dist
            union(parent,x,y)

    return result

result = solution(Edge)
print(total_price- result)
"""
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
"""