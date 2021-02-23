import sys
input = sys.stdin.readline
INF = int(1e9)
N = int(input())

max_val = 1
idx = 0
dp = [0]
while max_val < N+1:
    idx += 1

    if idx == 1 or idx == 2 or idx == 3 or idx == 5:
        dp.append(max_val)
        max_val += 1
    else:
        if idx%2 == 0:
            if dp[idx//2] != INF:
                dp.append(max_val)
                max_val += 1
                continue
        if idx % 3 == 0:
            if dp[idx // 3] != INF:
                dp.append(max_val)
                max_val += 1
                continue
        if idx % 5 == 0:
            if dp[idx // 5] != INF:
                dp.append(max_val)
                max_val += 1
                continue
        dp.append(INF)

print(idx)

