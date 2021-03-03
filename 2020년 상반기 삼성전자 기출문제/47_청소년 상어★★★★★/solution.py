
import copy

from collections import deque
import sys
input = sys.stdin.readline

dx = [0,-1,-1,0,1,1,1,0,-1]
dy = [0,0,-1,-1,-1,0,1,1,1]

board = []

for i in range(4):
    tmp = list(map(int,input().split()))
    board.append([[tmp[0],tmp[1]],[tmp[2],tmp[3]],[tmp[4],tmp[5]],[tmp[6],tmp[7]]])
    
def find_fish(board,idx):
    x,y,dir = 0,0,-1
    for i in range(4):
        for j in range(4):
            if board[i][j][0] == idx:
                x = i
                y = j
                dir = board[i][j][1]
                break
    return x,y,dir

def fish_move(board):
    for idx in range(1,17):
        x,y,dir = find_fish(board,idx)

        ##해당 숫자가 없는 경우
        if dir == -1:
            continue

        tmp_dir = dir
        while True:

            tmp_x = x+dx[tmp_dir]
            tmp_y = y+dy[tmp_dir]

            if 0<=tmp_x<4 and 0<=tmp_y <4:
                if board[tmp_x][tmp_y][0] != -1:
                    board[tmp_x][tmp_y] , board[x][y] = board[x][y] ,board[tmp_x][tmp_y]
                    board[tmp_x][tmp_y][1] = tmp_dir
                    break

            tmp_dir += 1
            if tmp_dir== 9: tmp_dir = 1
            if tmp_dir == dir:
                break

    return board

def solution(board):
    q = deque()
    result = 0
    s_x, s_y = 0,0
    s_dir = board[s_x][s_y][1]
    result += board[s_x][s_y][0]
    board[s_x][s_y][0] = -1
    q.append((board,result))
    max_value = -1

    while q:
        now_board, now_result= q.popleft()
        idx = 0

        if max_value < now_result: max_value = now_result

        #상어 찾기
        s_x,s_y,s_dir = find_fish(now_board,-1)

        now_board = fish_move(now_board)



        while True:
            idx += 1
            tmp_s_x, tmp_s_y = s_x+dx[s_dir]*idx, s_y+dy[s_dir]*idx
            tmp_board = copy.deepcopy(now_board)
            tmp_result = now_result
            if 0<=tmp_s_x<4 and 0<=tmp_s_y<4:
                if tmp_board[tmp_s_x][tmp_s_y][0] != 0:  #and tmp_board[tmp_s_x][tmp_s_y][0] != -1:
                    tmp_board[s_x][s_y][0] = 0
                    tmp_board[s_x][s_y][1] = 0

                    tmp_result += tmp_board[tmp_s_x][tmp_s_y][0]
                    tmp_board[tmp_s_x][tmp_s_y][0] = -1
                    q.append((tmp_board,tmp_result))
            else:
                break
    return max_value

result = solution(board)
print(result)













