# 행의 개수 N, 열의개수 M
N, M = map(int,input().split())
data = []
result = 0
minimum = 99999
tmp_min = 0
for i in range(N):
  tmp = list(map(int,input().split()))
  tmp_min = min(tmp)
  if minimum>tmp_min:
    minimum = tmp_min
  elif minimum<tmp_min:
    result = tmp_min
  data.append(tmp)

print(result)
