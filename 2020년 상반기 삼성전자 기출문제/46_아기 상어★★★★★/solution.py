import time
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
board = []




for i in range(N):
    tmp = list(map(int,input().split()))
    board.append(tmp)
    for k in range(len(tmp)):
        if tmp[k] == 9:
            board[i][k] = 0
            s_x = i
            s_y = k

dxy = [[0,1],[0,-1],[1,0],[-1,0]]

def BFS(board,s_x,s_y,s_lv):
    visited = [[-1 for _ in range(N)]for _ in range(N)]
    q = deque()
    q.append((s_x,s_y))
    visited[s_x][s_y] = 0
    while q:
        now_x, now_y = q.popleft()

        for dt in dxy:
            tmp_x,tmp_y = now_x + dt[0] , now_y + dt[1]
            if 0<=tmp_x<N and 0<=tmp_y<N and visited[tmp_x][tmp_y] == -1 and board[tmp_x][tmp_y] <= s_lv:
                visited[tmp_x][tmp_y] = visited[now_x][now_y] + 1
                q.append((tmp_x,tmp_y))
    return visited



def eat(visited,s_lv):
    min_val = 1e9
    min_x = 0
    min_y = 0
    is_EAT = False

    for i in range(N):
        for j in range(N):
            if board[i][j] != 0 and visited[i][j] != -1 and board[i][j] < s_lv:
                if min_val > visited[i][j]:
                    min_val = visited[i][j]
                    min_x, min_y = i, j
                    #print("Find", min_x, min_y, min_val)
    if min_val != 1e9:
        #print("Find")
        is_EAT = True
        board[min_x][min_y] =0
    return board, min_x, min_y,is_EAT

def solution(board):
    s_lv,cnt =2, 0
    min_x = s_x
    min_y = s_y
    result = 0
    while True:
        #print("입장",min_x,min_y,s_lv)
        visited = BFS(board,min_x, min_y, s_lv)
        board, min_x, min_y, is_EAT = eat(visited, s_lv)
        if is_EAT:
            result += visited[min_x][min_y]
            cnt += 1
            if cnt == s_lv:
                cnt = 0
                s_lv += 1
        else:
            break

    return result

result = solution(board)
print(result)











