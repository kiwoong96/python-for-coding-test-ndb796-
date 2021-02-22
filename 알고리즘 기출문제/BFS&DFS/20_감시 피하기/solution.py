import copy
from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
board = []
teacher = []
nobody = []
for i in range(N):
    tmp = list(input().split())
    board.append(tmp)
    for s in range(len(tmp)):
        if tmp[s] == 'T':
            teacher.append((i,s))
        elif tmp[s] == 'X':
            nobody.append((i,s))

dxy = [[0,1],[0,-1],[1,0],[-1,0]]

def check(teacher,board):
    q = deque()
    for tx,ty in teacher:
        for i in range(len(dxy)):
            tmp_x, tmp_y = tx + dxy[i][0], ty + dxy[i][1]
            if 0 <= tmp_x < N and 0 <= tmp_y < N :
                if board[tmp_x][tmp_y] == 'X':
                    q.append((i, tmp_x, tmp_y))
                elif board[tmp_x][tmp_y] == 'S':
                    return False

    while q:

        dir,x,y = q.popleft()
        tmp_x, tmp_y = x+dxy[dir][0], y+dxy[dir][1]
        if 0<= tmp_x< N and 0<=tmp_y<N:
            if board[tmp_x][tmp_y] == 'X':
                q.append((dir, tmp_x, tmp_y))
            elif board[tmp_x][tmp_y] == 'S':
                return False
    return True


def solution(board,teacher,nobody):
    nobody_comb = list(combinations(nobody,3))
    for n in nobody_comb:
        for nx,ny in n:
            board[nx][ny] = 'O'

        result = check(teacher,board)

        if result == False:
            for nx, ny in n:
                board[nx][ny] = 'X'
            continue
        else:
            return True


result = solution(board,teacher,nobody)
if result == True:
    print("YES")
else:
    print("NO")

