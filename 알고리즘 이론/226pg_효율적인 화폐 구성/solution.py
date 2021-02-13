N, M = map(int,input().split())

coins = []
d = [10001] * 10001
d[0] = 0
for i in range(N):
    coins.append(int(input()))


for i in range(N):
    #print("coins[i] : ", coins[i])
    for j in range(coins[i],M+1):
        if d[j-coins[i]] != 10001:
            #print("Enter j : ", j )
            d[j] = min(d[j],d[j-coins[i]]+1)

if d[M] == 10001:
    print(-1)
else:
    print(d[M])
