from collections import deque
import sys
input = sys.stdin.readline

N,L,R = map(int,input().split())

board = []

for i in range(N):
    board.append(list(map(int,input().split())))


dxy = [[1,0],[-1,0],[0,1],[0,-1]]

def open(x,y,visited):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    result = []
    result.append((x,y))

    while q:
        x,y = q.popleft()
        for dt in dxy:
            tmp_x,tmp_y = x+dt[0],y+dt[1]
            if 0<=tmp_x<N and 0<=tmp_y<N and L<= abs(board[x][y]-board[tmp_x][tmp_y]) <=R and visited[tmp_x][tmp_y] == False:
                visited[tmp_x][tmp_y] = True
                q.append((tmp_x,tmp_y))
                result.append((tmp_x,tmp_y))

    return result,visited

def calc(board,team):
    for t in team:
        sum_val = 0
        for tx,ty in t:
            sum_val += board[tx][ty]
        sum_val //= len(t)

        for tx,ty in t:
            board[tx][ty] = sum_val
    return board

def solution(board):
    visited = [[False for _ in range(N)] for _ in range(N)]
    time = 0
    while True:
        result = []
        for i in range(N):
            for j in range(N):
                if visited[i][j] == False:
                    tmp, visited = open(i, j, visited)
                    result.append(tmp)

        if len(result) == N*N:
            break
        else:
            board = calc(board,result)
            time+=1

        for i in range(N):
            for j in range(N):
                visited[i][j] = False

    return time

time = solution(board)
print(time)



