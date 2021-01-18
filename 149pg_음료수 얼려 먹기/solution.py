N, M = map(int,input().split())
board = []

for i in range(N):
    board.append(list(map(int,input())))

#print(N,M,board)

result = 0

def DFS(board,x,y):
    if x<0 or x>=N or y<0 or y>=M:
        return False
    elif board[x][y] == 1:
        return False
    else:
        #print('{},{}방문'.format(x,y))
        board[x][y] = 1
        DFS(board, x -1, y)
        DFS(board, x, y-1)
        DFS(board,x+1,y)
        DFS(board,x,y+1)
        return True
        #DFS(list,x+1,y+1)



for i in range(N):
    for j in range(M):
        if DFS(board,i,j)==True:
            #print('{},{}시작점'.format(i,j))
            result += 1

print(result)