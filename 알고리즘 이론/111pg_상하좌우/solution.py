N = int(input())
data = list(input().split())
print(N)
x = 1
y = 1
for i in data:
  if i=="R":
    if y>=N:
      pass
    else:
      y +=1
  if i=="U":
    if x<=1:
      pass
    else:
      x -=1
  if i=="D":
    if x>=N:
      pass
    else:
      x +=1
  if i=="L":
    if y<=1:
      pass
    else:
      y -=1

print(x,y)

"""
N = int(input())
data = list(input().split())
x,y = 1,1

dx = [0,0,-1,1]
dy = [-1,1,0,0]
dir = ['L','R','U','D']

for i in data:
  nx,ny = 0, 0
  for j in range(len(dir)):
    if i == dir[j]:
      nx = x + dx[j]
      ny = y + dy[j]
      break
  
  if nx > N or nx < 1 or ny > N or ny < 1:
    continue
  else:
    x,y = nx,ny

print(x,y)
"""