from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int,input().split())

board = []
virus = [[]for _ in range(K+1)]

for i in range(N):
    tmp = list(map(int,input().split()))
    board.append(tmp)
    for j in range(len(tmp)):
        if tmp[j] != 0:
            virus[tmp[j]].append((i,j))


S,X,Y = map(int,input().split())

dxy = [[0,1],[0,-1],[1,0],[-1,0]]

def BFS(virus):
    q = deque()
    for v in range(len(virus)):
        for vx,vy in virus[v]:
            q.append((0,v,vx,vy))

    while q:
        time,idx, x,y = q.popleft()
        """     
        for boards in board:
            print(boards)
        print()
        """
        if time >=S:
            break

        for dt in dxy:
            tmp_x,tmp_y = x+ dt[0], y+dt[1]
            if 0<= tmp_x <N and  0<= tmp_y <N and board[tmp_x][tmp_y] == 0:
                board[tmp_x][tmp_y] = idx
                q.append((time+1,idx,tmp_x,tmp_y))


BFS(virus)
print(board[X-1][Y-1])
"""
3 3
1 0 2
0 0 0
3 0 0
2 3 2
"""