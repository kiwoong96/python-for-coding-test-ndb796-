#이진탐색 알고리즘
"""
def binary_search(array,target,start,end):
    while start <= end:
        mid = (start + end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


N = int(input())
array1 = list(map(int,input().split()))
M = int(input())
array2 = list(map(int,input().split()))
array1.sort()


for target in array2:
    result = binary_search(array1,target,0,N-1)
    if result == None:
        print("no", end= ' ')
    else:
        print("yes",end = ' ')

"""
#계수정렬 알고리즘
"""
N = int(input())
array1 = list(map(int,input().split()))
M = int(input())
array2 = list(map(int,input().split()))
array1.sort()

max_val = max(array1)
count = [0] * (max_val+1)

for data in array1:
    count[data] += 1

for find_data in array2:
    if count[find_data] != 0:
        print("yes",end = ' ')
    else:
        print("no", end = ' ')
"""

#set자료형을 이용한 데이터 유무 확인
N = int(input())
array1 = set(map(int,input().split()))

M = int(input())
array2 = list(map(int, input().split()))

for x in array2:
    if x in array1:
        print("yes",end = ' ')
    else:
        print("no",end = ' ')

