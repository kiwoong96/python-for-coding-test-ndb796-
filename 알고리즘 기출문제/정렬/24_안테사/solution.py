import sys
input = sys.stdin.readline

N = int(input())

data = list(map(int,input().split()))

data.sort()
print(data[(len(data)-1)//2])