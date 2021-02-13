N, M = map(int, input().split())
A, B, d = map(int, input().split())

Map = []
visited = [[0] * M for _ in range(N)]

for i in range(N):
    tmp = list(map(int, input().split()))
    Map.append(tmp)

print("input end")


def changeDir():
    global d
    if d == 0:
        d = 3
    else:
        d -= 1
    print("방향 전환", d)


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

tmp_x = 0
tmp_y = 0

count = 0
result = 1
visited[A][B] = 1
while (True):
    # 1.방향 전환
    changeDir()
    tmp_x = A + dx[d]
    tmp_y = B + dy[d]
    print('tmp_x : {}, tmp_y : {}'.format(tmp_x, tmp_y))
    if tmp_x < 0 or tmp_y < 0 or tmp_x >= M or tmp_y >= N or Map[tmp_x][tmp_y] == 1 or visited[tmp_x][tmp_y] == 1:
        count += 1
        print("해당방향이 바다이거나 이미 방문한 곳")
        if count == 4:
            tmp_x = A - dx[d]
            tmp_y = B - dy[d]
            print("네방향 모두 방문되거나 바다", A, B)
            if Map[tmp_x][tmp_y] == 1 or visited[tmp_x][tmp_y] == 1:
                print("게임종료")
                break
            else:
                A = tmp_x
                B = tmp_y
                print("한칸뒤로이동", A, B)
    else:
        A = tmp_x
        B = tmp_y
        count = 0
        result += 1
        visited[A][B] = 1
        print("한칸 전진", A, B, d)
    DD = int(input())

print(result)