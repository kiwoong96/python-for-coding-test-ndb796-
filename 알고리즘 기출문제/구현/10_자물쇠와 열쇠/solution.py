import copy
import sys
input = sys.stdin.readline



N = 3
M = 3

def rotate(key):
    new_key = [[0 for _ in range(len(key[0]))]for _ in range(len(key))]
    for i in range(len(key)):
        for j in range(len(key)):

            new_key[i][j] = key[len(key)-j-1][i]
    return new_key

def move(board,key):
    new_lock = [[0 for _ in range(3*N)] for _ in range(3*N)]

    for i in range(N):
        for j in range(N):
            new_lock[N+i][N+j] = board[i][j]

    for h in range(2*N):
        for w in range(2*N):
            cnt = 0
            for i in range(M):
                for j in range(M):
                    if new_lock[i][j] != key[i][j]:
                        cnt += 1



    return False

key = [[0,0,0],
       [1,0,0],
       [0,1,1]]

lock = [[1,1,1],
        [1,1,0],
        [1,0,1]]

#result = move(lock,key)
#print(result)

key2 = rotate(key)
print(key2)
result = move(lock,key2)
print(result)
