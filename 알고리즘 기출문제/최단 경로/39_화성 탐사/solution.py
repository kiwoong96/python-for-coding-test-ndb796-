import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
T = int(input())

dxy = [[-1,0],[1,0],[0,1],[0,-1]]

for _ in range(T):
    N = int(input())

    board = []
    for _ in range(N):
        board.append(list(map(int,input().split())))

    distance = [[INF for _ in range(N)] for _ in range(N)]
    distance[0][0] = board[0][0]

    q = []
    heapq.heappush(q,(board[0][0],0,0))

    while q:
        dist, x, y = heapq.heappop(q)


        if distance[x][y] < dist:
            continue

        for dt in dxy:
            tmp_x, tmp_y = x+dt[0], y+dt[1]
            if 0<=tmp_x<N and 0<=tmp_y<N:
                if distance[tmp_x][tmp_y] > dist+board[tmp_x][tmp_y]:
                    distance[tmp_x][tmp_y] = dist + board[tmp_x][tmp_y]
                    heapq.heappush(q,(distance[tmp_x][tmp_y],tmp_x,tmp_y))
    print(distance[N - 1][N - 1])


"""
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
"""

