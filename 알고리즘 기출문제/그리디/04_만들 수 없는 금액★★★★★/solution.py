import sys
input = sys.stdin.readline

N = int(input())

data = list(map(int,input().split()))

data.sort()

target = 1

for i in data:
    if target < i:
        break
    target += i

print(target)