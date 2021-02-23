import sys
input = sys.stdin.readline

N = int(input())
data = []
for i in range(N):
    tmp = list(input().split())
    data.append((tmp[0],int(tmp[1]),int(tmp[2]),int(tmp[3])))

data.sort(key = lambda x:(-x[1],x[2],-x[3],x[0]))

for i in data:
    print(i[0])
    