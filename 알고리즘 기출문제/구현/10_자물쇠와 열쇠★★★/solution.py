
\
def rotate(key):
    N = len(key)
    new_key = [[0 for _ in range(N)]for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_key[i][j] = key[N-j-1][i]
    return new_key


def check(new_lock):
    N = len(new_lock)//3
    for i in range(N,2*N):
        for j in range(N,2*N):
            if new_lock[i][j] != 1:
                return False

    return True

def solution(key,lock):
    N = len(lock)
    M = len(key)

    new_lock = [[0 for _ in range(3 * N)] for _ in range(3 * N)]
    for i in range(N):
        for j in range(N):
            new_lock[N + i][N + j] = lock[i][j]

    result = False

    for k in range(4):
        key = rotate(key)
        for h in range(2*N):
            for w in range(2*N):
                for i in range(M):
                    for j in range(M):
                        new_lock[i+h][j+w] += key[i][j]

                if check(new_lock) == True:
                    return True
                for i in range(M):
                    for j in range(M):
                        new_lock[i+h][j+w] -= key[i][j]


    return False

key = [[1,0,0,0],
       [0,0,1,0],
       [0,1,1,1],
       [1,1,1,1]]

lock = [[1,1,1],
        [1,1,0],
        [1,0,1]]

print(solution(key,lock))
