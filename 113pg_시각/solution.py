N = int(input())

count = 0

for H in range(N+1):
  for M in range(0,60):
    for S in range(0,60):
      time = str(H) + str(M) + str(S)
      if "3" in time:
        count += 1

print(count)
