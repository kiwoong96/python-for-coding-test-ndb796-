array = [7,5,9,0,3,1,6,2,4,8]
"""
for i in range(1,len(array)-1):
    tmp1 = array[i]
    idx = i
    for j in range(i,-1,-1):
        tmp2 = array[j]

        if tmp2 > tmp1:
            array[idx], array[j] = array[j] , array[idx]
            idx = j

print(array)
"""
for i in range(1,len(array)):
    for j in range(i,0,-1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1] , array[j]
        else:
            break
print(array)