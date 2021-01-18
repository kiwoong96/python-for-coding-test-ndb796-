array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

count = [0 for _ in range(max(array)+1)]

for val in array:
    count[val] += 1


for x in range(len(count)):
    for val in range(count[x]):
        print(x, end=' ')

