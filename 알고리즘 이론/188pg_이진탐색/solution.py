#재귀함수 풀이
"""
def binary_search(array, target, start, end):
    if start>end:
        return None
    mid = (start + end) // 2
    #print("array[mid] : ", array[mid],", start : ",start, ", end : ", end)
    if target == array[mid]:
        return mid + 1
    elif target > array[mid]:
        return binary_search(array,target,mid + 1,end)
    else:
        return binary_search(array,target,start,mid - 1)

n, target = list(map(int,input().split()))
array = list(map(int,input().split()))

result = binary_search(array,target,0,n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result)
"""

#반복문 코드

n, target = list(map(int,input().split()))
array = list(map(int,input().split()))

start = 0
end = n-1
def binary_search(array,target,start,end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

result = binary_search(array,target,start,end)
if result!=None:
    print(result)
else:
    print("원소가 존재하지 않습니다.")

