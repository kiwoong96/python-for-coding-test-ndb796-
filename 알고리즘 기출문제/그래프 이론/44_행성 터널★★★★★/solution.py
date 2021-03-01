import heapq
import sys
input = sys.stdin.readline

N = int(input())



Edge = []
x = []
y = []
z = []

for i in range(N):
    a,b,c = map(int,input().split())
    x.append((a,i))
    y.append((b,i))
    z.append((c,i))

x.sort()
y.sort()
z.sort()

for i in range(N-1):
    heapq.heappush(Edge,(abs(x[i][0]-x[i+1][0]),x[i][1],x[i+1][1]))
    heapq.heappush(Edge,(abs(y[i][0] - y[i + 1][0]),y[i][1],y[i+1][1]))
    heapq.heappush(Edge,(abs(z[i][0] - z[i + 1][0]),z[i][1],z[i+1][1]))





def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b



def solution(Edge):
    parent = [i for i in range(N)]
    result = 0
    while Edge:
        now = heapq.heappop(Edge)
        dist,x,y = now[0], now[1], now[2]

        if find_parent(parent,x) != find_parent(parent,y):
            union(parent,x,y)
            result += dist
    return result

result = solution(Edge)
print(result)

