import sys
input = sys.stdin.readline

data = input()

result = [0,0]
before = data[0]

for i in range(1,len(data)):
    if data[i] == before:
        continue
    else:
        result[int(before)] += 1
        before = data[i]

print(result)