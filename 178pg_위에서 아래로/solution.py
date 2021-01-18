n = int(input())
list = []
for i in range(n):
    list.append(int(input()))

result = sorted(list, reverse=True)

for i in result:
    print(i,end=' ')
