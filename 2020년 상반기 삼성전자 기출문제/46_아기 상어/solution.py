from collections import deque
import heapq
import sys
input = sys.stdin.readline

#8:56~9:24


N = int(input())

fish = []
shark = []
board = []

for i in range(N):
    tmp = list(map(int,input().split()))
    board.append(tmp)
    for k in range(len(tmp)):
        if tmp[k] == 9:
            shark.append((i,k))
        if tmp[k] != 0:
            fish.append((tmp[k],i,k))

fish.sort()

dxy = [[0,1],[0,-1],[1,0],[-1,0]]


def solution(fish,shark):
    s_x = shark[0][0]
    s_y = shark[0][1]
    s_lv = 2
    q = deque()
    cnt = 0
    q.append((s_x,s_y,s_lv,cnt))

    while q:
        print(fish)
        s_x,s_y,s_lv,cnt = q.popleft()
        for dt in dxy:
            tmp_s_x ,tmp_s_y = s_x + dt[0], s_y + dt[1]
            if 0<=tmp_s_x<N and 0<=tmp_s_y <N:
                if board[tmp_s_x][tmp_s_y] == 0:
                    q.append((tmp_s_x, tmp_s_y, s_lv, cnt))

                elif board[tmp_s_x][tmp_s_y] < s_lv:
                    print(board[tmp_s_x][tmp_s_y], tmp_s_x, tmp_s_y)
                    fish.remove(( board[tmp_s_x][tmp_s_y], tmp_s_x, tmp_s_y))

                    cnt += 1
                    board[tmp_s_x][tmp_s_y] = 0


                    if cnt == s_lv :
                        s_lv +=1
                        cnt = 0
                    q.append((tmp_s_x,tmp_s_y,s_lv,cnt))
                elif board[tmp_s_x][tmp_s_y] == s_lv:
                    q.append((tmp_s_x, tmp_s_y, s_lv, cnt))
                else:
                    continue
solution(fish,shark)