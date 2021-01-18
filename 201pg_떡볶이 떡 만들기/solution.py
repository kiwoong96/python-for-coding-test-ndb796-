N, M = map(int,input().split())
array = list(map(int,input().split()))

def binary_search(array,target,start,end):
    while start <= end:
        mid = (start + end)//2
        sum = 0
        for i in array:
            if i>mid:
                sum += i-mid
        #print("sum : " , sum, " mid : " , mid)
        if sum == target:
            #print("찾았습니다!")
            return mid
        elif sum > target:
            #print("오른쪽으로 이동")
            start = mid + 1
        else:
            #print("왼쪽으로 이동")
            end = mid - 1
    return None

start = 0
end = max(array)
print("end : " , end)
result = binary_search(array,M,start,end)
print(result)
