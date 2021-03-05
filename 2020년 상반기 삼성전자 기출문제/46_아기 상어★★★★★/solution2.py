import time
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

board = []
s_x,s_y = 0,0
s_lv = 2
for i in range(N):
    tmp = list(map(int,input().split()))
    for j in range(len(tmp)):
        if tmp[j] == 9:
            s_x,s_y = i,j
            tmp[j] = 0
    board.append(tmp)

def print_board(board):
    for data in board:
        print(data)
    print()

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def find(board,s_x,s_y,s_lv):
    new_board = [[-1 for _ in range(N)] for _ in range(N)]
    q = deque()
    q.append((s_x,s_y))
    new_board[s_x][s_y] = 0

    while q:
        x,y = q.popleft()

        for i in range(4):
            tmp_x,tmp_y = x+dx[i],y+dy[i]

            if 0<=tmp_x<N and  0<=tmp_y<N and new_board[tmp_x][tmp_y] == -1 and board[tmp_x][tmp_y] <= s_lv:
                new_board[tmp_x][tmp_y] = new_board[x][y] + 1
                q.append((tmp_x,tmp_y))

    return new_board


def solution(board,s_x,s_y,s_lv):
    count = 0
    result = 0

    while True:
        is_Find = False
        min_val = 1e9

        new_board = find(board,s_x,s_y,s_lv)

        for i in range(N):
            for j in range(N):
                if new_board[i][j]!=-1 and board[i][j]<s_lv and board[i][j]!=0:
                    if min_val > new_board[i][j]:
                        min_val = new_board[i][j]
                        s_x,s_y = i,j
                        is_Find = True


        if is_Find:
            result += new_board[s_x][s_y]
            board[s_x][s_y] = 0
            count += 1
            if count == s_lv:
                s_lv +=1
                count = 0
        else:
            break

    return result




result = solution(board,s_x,s_y,s_lv)

print(result)