from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline
INF = int(1e9)
N,M = map(int,input().split())

board = []
virus = []
no_virus = []

for i in range(N):
    tmp = list(map(int,input().split()))
    board.append(tmp)
    for j in range(len(tmp)):
        if tmp[j] == 0:
            no_virus.append((i,j))
        elif tmp[j] == 2:
            virus.append((i,j))

dxy = [[0,1],[0,-1],[1,0],[-1,0]]

def BFS(v_x,v_y,visited):

    q = deque()
    q.append((v_x,v_y))
    visited[v_x][v_y] = True
    result = 0
    while q:
        x,y = q.popleft()
        for dt in dxy:
            tmp_x, tmp_y = x+dt[0],y+dt[1]
            if 0<= tmp_x <N and 0<=tmp_y <M and board[tmp_x][tmp_y] == 0 and visited[tmp_x][tmp_y] == False:
                visited[tmp_x][tmp_y] = True
                q.append((tmp_x,tmp_y))
                result += 1

    return result, visited

no_virus_comb = list(combinations(no_virus,3))
min_val = INF

for v in no_virus_comb:
    result = 0
    for nvx, nvy in v:
        board[nvx][nvy] = 1

    visited = [[False for _ in range(M)] for _ in range(N)]
    #print(board)
    for vx, vy in virus:
        tmp_result, visited = BFS(vx,vy,visited)
        result += tmp_result
    if min_val > result:
        min_val = result

    for nvx, nvy in v:
        board[nvx][nvy] = 0

print(len(no_virus)-3-min_val)



