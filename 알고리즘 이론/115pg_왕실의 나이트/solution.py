start = input()

dx = [1,-1,1,-1,2,2,-2,-2]
dy = [2,2,-2,-2,1,-1,1,-1]

x = ord(start[0])-96
y = int(start[1])

tmp_x = 0
tmp_y = 0
count = 0

for i in range(8):
  tmp_x = x + dx[i]
  tmp_y = y + dy[i]
  if tmp_x <= 8 and tmp_x >=1 and tmp_y <=8 and tmp_y >= 1:
    #print(tmp_x,tmp_y,i)
    count +=1

print(count)