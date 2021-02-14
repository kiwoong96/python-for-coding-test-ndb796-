import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int,input().split()))

data.sort()

count = 0
result = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)


