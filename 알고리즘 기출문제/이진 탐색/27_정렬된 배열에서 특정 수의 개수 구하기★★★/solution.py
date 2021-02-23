"""
import sys
input = sys.stdin.readline

N, x = map(int,input().split())

data = list(map(int,input().split()))


while len(data) > 1:
    result = 0
    if data[len(data)//2] == x:
        for i in data:
            if i == 2:
                result += 1
        break
    elif data[len(data)//2] > x:
        data = data[:(len(data)-1)//2]
    else:
        data = data[len(data)//2:]
    print(data)
if result == 0:
    print(-1)
else:
    print(result)
"""

from bisect import bisect_left,bisect_right
import sys
input = sys.stdin.readline

N, x = map(int,input().split())

data = list(map(int,input().split()))

start = bisect_left(data,x)
end = bisect_right(data,x)


if end-start == 0:
    print(-1)
else:
    print(end-start)