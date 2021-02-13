n = int(input())

list = []

for i in range(n):
    input_data = input().split()
    list.append((input_data[0],int(input_data[1])))

result = sorted(list,key = lambda student:student[1])

for x in result:
    print(x[0],end=' ')