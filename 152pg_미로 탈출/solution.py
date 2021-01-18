from collections import deque

N, M = map(int,input().split())

data = []

for _ in range(N):
    data.append(list(map(int,input())))

print(data)

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def BFS(data):
    queue = deque()
    x = 0
    y = 0
    D = 1
    queue.append((x,y,D))
    while queue:
        tmp = queue.popleft()
        x = tmp[0]
        y = tmp[1]
        D = tmp[2] + 1
        for i in range(4):
            tmp_x = x+dx[i]
            tmp_y = y+dy[i]
            if tmp_x < 0 or tmp_y < 0 or tmp_x >= N or tmp_y >= M:
                continue
            elif data[tmp_x][tmp_y] ==1:
                if tmp_x == 0 and tmp_y == 0:
                    continue
                else:
                    print('({},{})방문 값 = {}'.format(tmp_x, tmp_y, D))
                    data[tmp_x][tmp_y] = D
                    ##여기에 return 조건을 넣으면 빠르게 종료
                    ##바깥에 return 조건을 넣으면 가능한 경로 모두 탐색후 종료
                    queue.append((tmp_x, tmp_y,D))
    return data[N-1][M-1]

print(BFS(data))


