from itertools import combinations
import sys
input = sys.stdin.readline
INF = int(1e9)

N,M = map(int,input().split())

board = []
house = []
chicken_shop = []

for i in range(N):
    data = list(map(int,input().split()))
    for k in range(len(data)):
        if data[k] == 1:
            house.append((i,k))
        elif data[k] == 2:
            chicken_shop.append((i,k))

candidates = list(combinations(chicken_shop,M))


def solution(candidates):
    result = INF

    for candidate in candidates:
        tmp = [INF for _ in range(len(house))]
        for cx,cy in candidate:
            for k in range(len(house)):
                hx,hy = house[k][0],house[k][1]
                tmp[k] = min(tmp[k], abs(hx - cx) + abs(hy - cy))
        if sum(tmp) < result:
            result = sum(tmp)
    return result

result = solution(candidates)
print(result)


#0 : 빈칸
#1 : 집
#2 : 치킨집


