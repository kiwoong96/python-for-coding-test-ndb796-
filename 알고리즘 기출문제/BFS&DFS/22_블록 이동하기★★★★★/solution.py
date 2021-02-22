from collections import deque

dx = [-1,1]
dy = [1,-1]
dxy = [[1,0],[-1,0],[0,1],[0,-1]]

##가로->세로
def rotate_1(board,x1,y1,x2,y2):
    N = len(board)
    result = []
    for dt in dx:
        tmp_x1,tmp_x2 = x1+dt, x2+dt
        if 0<=tmp_x1<N and 0<=tmp_x2<N and board[tmp_x1][y1] == 0 and board[tmp_x2][y2]==0:
            result.append((x1,y1,tmp_x1,y1))
            result.append((x2,y2,tmp_x2,y2))
    return result

##세로->가로
def rotate_2(board,x1,y1,x2,y2):
    N = len(board)
    result = []
    for dt in dy:
        tmp_y1,tmp_y2 = y1+dt,y2+dt
        if 0<=tmp_y1<N and 0<=tmp_y2<N and board[x1][tmp_y1] == 0 and board[x2][tmp_y2] == 0:
            result.append((x1,y1,x1,tmp_y1))
            result.append((x2,y2,x2,tmp_y2))
    return result

board = [[0, 0, 1, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0],
         [1, 0, 0, 0, 1, 1, 0],
         [1, 0, 0, 0, 1, 1, 0],
         [1, 0, 1, 1, 1, 1, 0],
         [1, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 1, 1, 0, 0]]

def solution(board):
    N = len(board)
    q = deque()
    visited = set()
    time = 0
    #dir : 0 (가로방향)
    #dir : 1 (세로방향)
    q.append((time,0,0,0,0,1))
    visited.add((0,0,0,1))


    while q:
        time,dir,x1,y1,x2,y2 = q.popleft()
        if (x1==N-1 and y1== N-1) or (x2 == N-1 and y2 == N-1):
            return time

        for dt in dxy:
            tmp_x1,tmp_y1,tmp_x2,tmp_y2 = x1+dt[0],y1+dt[1],x2+dt[0],y2+dt[1]
            if 0<=tmp_x1<N and 0<=tmp_y1<N and 0<=tmp_x2<N and 0<=tmp_y2<N:
                if board[tmp_x1][tmp_y1] == 0 and board[tmp_x2][tmp_y2] == 0 and (tmp_x1,tmp_y1,tmp_x2,tmp_y2) not in visited:
                    visited.add((tmp_x1,tmp_y1,tmp_x2,tmp_y2))
                    q.append((time+1, dir, tmp_x1, tmp_y1, tmp_x2, tmp_y2))
        if dir == 0:
            turn1 = rotate_1(board,x1,y1,x2,y2)
            if turn1:
                for tmp_x1, tmp_y1, tmp_x2, tmp_y2 in turn1:
                    if (tmp_x1, tmp_y1, tmp_x2, tmp_y2) not in visited:
                        visited.add((tmp_x1, tmp_y1, tmp_x2, tmp_y2))
                        q.append((time + 1, 1, tmp_x1, tmp_y1, tmp_x2, tmp_y2))
        elif dir == 1:
            turn2 = rotate_2(board, x1, y1, x2, y2)
            if turn2:
                for tmp_x1, tmp_y1, tmp_x2, tmp_y2 in turn2:
                    if (tmp_x1, tmp_y1, tmp_x2, tmp_y2) not in visited:
                        visited.add((tmp_x1, tmp_y1, tmp_x2, tmp_y2))
                        q.append((time + 1, 0, tmp_x1, tmp_y1, tmp_x2, tmp_y2))
        print(q)


result = solution(board)
print(result)