import sys
input = sys.stdin.readline

S = input().strip('\n')

result = [0,0]

for i in range(len(S)):
    if i< len(S)//2:
        result[0] +=int(S[i])
    else:
        result[1] +=int(S[i])


if result[0] == result[1]:
    print("LUCKY")
else:
    print("READY")