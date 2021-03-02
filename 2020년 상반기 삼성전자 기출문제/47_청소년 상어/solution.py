import copy
import heapq
from collections import deque
import sys
input = sys.stdin.readline

dxy = [[0,0],[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]


board = []
fish = []

for j in range(4):
    tmp = list(map(int,input().split()))
    for i in range(4):
        board.append((tmp[i*2],tmp[i*2+1]))
    for i in range(4):
        if j==0 and i ==0 : continue
        heapq.heappush(fish, (tmp[i*2],tmp[i*2+1],j,i))


for i in range(4):
    print(board[i*4:i*4+4])

def fish_move(board,fish):
    while fish:
        fish_val,fish_dir,x,y = heapq.heappop(fish)

        tmp_x, tmp_y = x+dxy[fish_dir][0], y+dxy[fish_dir][1]

        if 0<=tmp_x<4 and 0<=tmp_y<4 and board[tmp_x][tmp_y] != 0 and board[tmp_x][tmp_y] != -1:
            board[tmp_x][tmp_y], board[x][y] =  board[x][y], board[tmp_x][tmp_y]
        # 밖을 벗어나거나 / 비어있거나 / 상어가 있는 경우
        else:
            dir += 1
            if dir == 9: dir = 1
            board[x][y][1] = dir
            heapq.heappush(fish,(board[x][y][0], board[x][y][1],x,y))

    for i in range(4):
        for j in range(4):
            if board[i][j] != 0 and board[i][j] != -1:
                heapq.heappush(fish,(board[i][j][0],board[i][j][1],i,j))
    return board, fish



def BFS(board,fish):
    q = deque()
    s_x, s_y, cnt ,s_dir = 0,0 , board[0][0][0],board[0][0][1]
    q.append((board,fish,cnt,s_dir))
    board[s_x][s_y] = -1

    while q:
        now = q.popleft()
        now_board, now_fish, now_cnt, now_dir = now[0], now[1], now[2], now[3]
        now_board, now_fish = fish_move(now_board,now_fish)
        idx = 0
        while True:
            idx += 1
            tmp_x , tmp_y = s_x + dxy[s_dir][0]*idx ,s_y + dxy[s_dir][1]*idx
            count = 0
            if 0<=tmp_x<4 and 0<=tmp_y<4:
                if board[tmp_x][tmp_y] != 0:
                    tmp_fish = copy.deepcopy(now_fish)
                    tmp_fish.remove(now_board[tmp_x][tmp_y][0], now_board[tmp_x][tmp_y][1], tmp_x, tmp_y)
                    tmp_cnt = copy.deepcopy(now_cnt)
                    tmp_cnt += now_board[tmp_x][tmp_y][0]
                    now_dir = now_board[tmp_x][tmp_y][1]
                    tmp_board = copy.deepcopy(now_board)
                    tmp_board[tmp_x][tmp_y] = -1
                    q.append(tmp_board,tmp_fish,tmp_cnt,now_dir)
                    count +=1
            else:
                break






