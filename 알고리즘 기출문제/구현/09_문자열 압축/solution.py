import sys
input = sys.stdin.readline

s = 'abcabcdede'

def solution(s):
    min_value = 1e9
    length = len(s)
    for i in range(1,length//2+1):
        cut = i
        j = 1
        before = s[0:i*j]
        isFirst = True
        result = cut
        while i*(j+1) <= length:
            now = s[i*j:i*(j+1)]
            if before==now and isFirst:     #처음 겹치는경우
                result += 1
                isFirst = False
            elif before!=now:
                result += i
                isFirst = True
            j += 1

            #print("before : ",before, ", now : ", now, ", result : ", result, ", isFirst : ",isFirst)
            before = now
        if i*(j+1) > length:
            result += length-i*j
        if min_value > result:
            min_value = result


    return min_value


result = solution(s)
print(result)