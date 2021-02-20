from collections import deque

import sys

input = sys.stdin.readline


def solution(board, direction):
    dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    queue = deque()
    dir = 0
    x, y = 0, 0
    queue.append((x,y))
    board[x][y] = 2
    time = 1

    # 오른쪽으로 이동하면 dir +1 3에서 오른쪽이면 0으로 초기화
    # 왼쪽으로 이동하면 dir -1 0에서 왼쪽이면 3으로 초기화
    # 0 : 비어있는 공간
    # 1 : 사과가 있는 공간
    # 2 : 뱀의 몸통이 있는 공간

    while True:
        tmp_x, tmp_y = x + dxy[dir][0], y + dxy[dir][1]
        if tmp_x < 0 or tmp_y < 0 or tmp_x >= N or tmp_y >= N or board[tmp_x][tmp_y] == 2:
            break

        x,y = tmp_x,tmp_y
        if board[x][y] == 1:
            board[x][y] = 2
            queue.append((x,y))

        elif board[x][y] == 0:
            board[x][y] = 2
            tmp = queue.popleft()
            before_x, before_y = tmp[0],tmp[1]
            board[before_x][before_y] = 0
            queue.append((x,y))

        if direction and direction[0][0] == time:
            change = direction.popleft()[1]
            #방향이 오른쪽
            if change == 'D':
                if dir == 3:
                    dir = 0
                else:
                    dir += 1
            else:
                if dir == 0:
                    dir = 3
                else:
                    dir -= 1

        time += 1


    return time


N = int(input())
K = int(input())

board = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(K):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1

direction = deque()

L = int(input())
for _ in range(L):
    a, b = list(input().split())
    direction.append((int(a), b))

time = solution(board,direction)
print(time)