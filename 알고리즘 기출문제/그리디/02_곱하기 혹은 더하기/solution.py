import sys
input = sys.stdin.readline

data= input().strip('\n')

result = int(data[0])

for i in range(1,len(data)):
    now = int(data[i])
    if result==0 or result==1 or now ==0 or now==1:
        result += now
    else:
        result *= now

print(result)


