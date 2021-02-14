"""import sys
input = sys.stdin.readline

N, M = map(int,input().split())
data = list(map(int,input().split()))

data.sort()

tmp = 1
before = 0
sumation = 0

for i in data:
    if before == i:
        tmp += 1
    else:
        if tmp >= 2:
            sumation += tmp * (tmp - 1) // 2
        tmp = 1
        before = i
    if data[-1] == i:
        if tmp >= 2:
            sumation += tmp * (tmp - 1) // 2

result = N*(N-1)//2 - sumation

print(result)"""

import sys
input = sys.stdin.readline

N,M = map(int,input().split())

data =list(map(int,input().split()))

Ball = [0 for _ in range(N+1)]

for i in data:
    Ball[i] += 1

result = 0

for i in range(1,N+1):
    N -= Ball[i]
    result += Ball[i]*N

print(result)