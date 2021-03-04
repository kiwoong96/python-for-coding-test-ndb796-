from collections import deque
import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())

board = [[[]for _ in range(N)] for _ in range(N)]


dx = [0,-1,1,0,0]
dy = [0,0,0,-1,1]

for i in range(N):
    tmp = list(map(int,input().split()))
    for j in range(len(tmp)):
        if tmp[j] !=0:
            board[i][j].append(True)
            board[i][j].append(tmp[j])
            board[i][j].append(K)
            board[i][j].append(0)     ##상어의 존재유무, 상어의 번호,간 냄새의 남은 시간, 방향
        else:
            board[i][j].append(False)
            board[i][j].append(0)
            board[i][j].append(0)
            board[i][j].append(0)

def find_shark(board,idx):
    x,y,dir = 0,0,-1
    for i in range(N):
        for j in range(N):
            if board[i][j][0] == True and board[i][j][1] == idx:
                x = i
                y = j
                dir = board[i][j][3]

    return x,y,dir


tmp = list(map(int,input().split()))
for idx in range(len(tmp)):
    x,y,dir = find_shark(board,idx+1)
    board[x][y][3] = tmp[idx]
shark_dir = [[]for _ in range(M+1)]

for i in range(1,M+1):
    for j in range(4):
        tmp = list(map(int,input().split()))
        shark_dir[i].append(tmp)


def print_board(board):
    for i in board:
        print(i)
    print()

"""
for i in shark_dir:
    print(i)
print()
"""
def move_shark(board):
    q = deque()
    for idx in range(1,M+1):
        is_move = False
        x,y,dir = find_shark(board,idx)
        if dir == -1:
            continue
        for i in range(4):
            tmp_dir = shark_dir[idx][dir-1][i]
            tmp_x = x + dx[tmp_dir]
            tmp_y = y + dy[tmp_dir]
            if 0<=tmp_x<N and 0<=tmp_y<N and board[tmp_x][tmp_y][1] == 0:
                q.append((idx,tmp_x,tmp_y,tmp_dir))
                is_move = True
                break
            else:
                continue

        if not is_move:
            for i in range(4):
                tmp_dir = shark_dir[idx][dir-1][i]
                tmp_x = x + dx[tmp_dir]
                tmp_y = y + dy[tmp_dir]

                if 0 <= tmp_x < N and 0 <= tmp_y < N and board[tmp_x][tmp_y][1] == idx:
                    q.append((idx, tmp_x, tmp_y, tmp_dir))
                    is_move = True
                    break
                else:
                    continue


    for i in range(N):
        for j in range(N):
            if board[i][j][0] == True:
                board[i][j][0] = False
                board[i][j][2] = K
                board[i][j][3] = 0

    while q:
        idx, tmp_x,tmp_y,tmp_dir = q.popleft()
        if board[tmp_x][tmp_y][0] == False:
            board[tmp_x][tmp_y][0] = True
            board[tmp_x][tmp_y][1] = idx
            board[tmp_x][tmp_y][2] = K
            board[tmp_x][tmp_y][3] = tmp_dir
        else:
            continue
    return board

def one_time(board):
    for i in range(N):
        for j in range(N):
            if board[i][j][0] == False and board[i][j][1] != 0:
                board[i][j][2] -= 1
                if board[i][j][2] == 0:
                    board[i][j][1] = 0
                    board[i][j][3] = 0
    return board

def check_is_finish(board):
    result = True
    for idx in range(2,M+1):
        x,y,dir = find_shark(board,idx)
        if dir == -1:
            continue
        else:
            result = False
            break
    return result









def solution(board):
    count = 0
    #print_board(board)
    while count <= 1000:
        count += 1
        #print(count, " 번째!")
        board = move_shark(board)
        #print_board(board)
        board = one_time(board)
        #print_board(board)
        is_finish = check_is_finish(board)
        if is_finish:
            break
    return count

count  = solution(board)
if count == 1001:
    print(-1)
else:
    print(count)



