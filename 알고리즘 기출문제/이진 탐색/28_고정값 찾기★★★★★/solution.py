from bisect import bisect_right, bisect_left
import sys
input = sys.stdin.readline


N = int(input())
data = list(map(int,input().split()))

result = -1

length = len(data)
find_idx = length//2
find_value
tmp = 0
while data:
    if find_idx == data[find_idx]:
        result = find_idx
        break
    elif find_idx > data[find_idx]:
        data = data[find_idx:]
        
    elif find_idx < data[find_idx]:
        data = data[:find_idx]
