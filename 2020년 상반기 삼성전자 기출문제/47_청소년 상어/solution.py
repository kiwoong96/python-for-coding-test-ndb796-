import time
import copy
import heapq
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
                if board[tmp_x][tmp_y][0] != 0 and board[tmp_x][tmp_y][0] != -1:
                    board[tmp_x][tmp_y] , board[x][y] = board[x][y] ,board[tmp_x][tmp_y]
                    board[tmp_x][tmp_y][1] = tmp_dir
                    break

            tmp_dir += 1
            if tmp_dir== 9: tmp_dir = 1
            if tmp_dir == dir:
                break
        print("idx : ", idx)
        for i in board:
            print(i)
        print()
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
        print(s_x,s_y,s_dir)

        now_board = fish_move(now_board)
        """for i in now_board:
            print(i)
        print()"""

        #time.sleep(5)
        while True:
            idx += 1
            tmp_s_x, tmp_s_y = s_x+dx[s_dir]*idx, s_y+dy[s_dir]*idx
            print(tmp_s_x, tmp_s_y)
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













"""
for j in range(4):
    tmp = list(map(int,input().split()))
    board.append([[tmp[0],tmp[1]],[tmp[2],tmp[3]],[tmp[4],tmp[5]],[tmp[6],tmp[7]]])
    for i in range(4):
        if j==0 and i ==0 : continue
        heapq.heappush(fish, (tmp[i*2],tmp[i*2+1],j,i))







def fish_move(board,fish):
    while fish:

        fish_val,fish_dir,x,y = heapq.heappop(fish)
        print("Fish 동")
        print(fish_val, fish_dir, x, y)
        for i in board:
            print(i)
        print()
        tmp_x, tmp_y = x+dxy[fish_dir][0], y+dxy[fish_dir][1]

        if 0<=tmp_x<4 and 0<=tmp_y<4 and board[tmp_x][tmp_y] != 0 and board[tmp_x][tmp_y] != -1:
            board[tmp_x][tmp_y], board[x][y] =  board[x][y], board[tmp_x][tmp_y]
            fish.remo
        # 밖을 벗어나거나 / 비어있거나 / 상어가 있는 경우
        else:
            fish_dir += 1
            if fish_dir == 9: fish_dir = 1
            board[x][y][1] = fish_dir
            heapq.heappush(fish,(board[x][y][0], board[x][y][1],x,y))

    for i in range(4):
        for j in range(4):
            if board[i][j] != 0 and board[i][j] != -1:
                heapq.heappush(fish,(board[i][j][0],board[i][j][1],i,j))
    return board, fish



def BFS(board,fish):
    q = deque()
    s_x, s_y, cnt ,s_dir = 0,0,board[0][0][0],board[0][0][1]
    q.append((board,fish,cnt,s_dir,s_x,s_y))
    board[s_x][s_y] = -1
    result = -1

    while q:
        now = q.popleft()
        now_board, now_fish, now_cnt, now_dir,now_x,now_y = now[0], now[1], now[2], now[3],now[4],now[5]
        now_board, now_fish = fish_move(now_board,now_fish)

        print("현재보드!", "방향 : " ,now_dir)
        for i in now_board:
            print(i)
        print()

        if now_cnt > result: result = now_cnt
        idx = 0
        count = 0
        while True:
            idx += 1
            tmp_x , tmp_y = now_x + dxy[now_dir][0]*idx ,now_y + dxy[now_dir][1]*idx
            if 0<=tmp_x<4 and 0<=tmp_y<4:
                if now_board[tmp_x][tmp_y] != 0:
                    count +=1
                    tmp_fish = copy.deepcopy(now_fish)
                    print(tmp_x,tmp_y,now_x,now_y)
                    tmp_fish.remove((now_board[tmp_x][tmp_y][0], now_board[tmp_x][tmp_y][1], tmp_x, tmp_y))
                    tmp_cnt = copy.deepcopy(now_cnt)
                    tmp_cnt += now_board[tmp_x][tmp_y][0]
                    tmp_dir = now_board[tmp_x][tmp_y][1]
                    tmp_board = copy.deepcopy(now_board)
                    tmp_board[tmp_x][tmp_y] = -1
                    tmp_board[now_x][now_y] = 0
                    q.append((tmp_board,tmp_fish,tmp_cnt,tmp_dir,tmp_x,tmp_y))
                    count +=1
                    print("이동할 보드!")
                    for k in tmp_board:
                        print(k)
                    print()

            else:
                break

    return result

for k in board:
    print(k)

result = BFS(board,fish)
print(result)
"""



