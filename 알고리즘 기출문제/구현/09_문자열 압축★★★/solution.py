import sys
input = sys.stdin.readline

s = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxz'

def solution(s):
    min_value = len(s)
    length = len(s)
    aa = 1
    for i in range(1,length//2+1):
        j = 1
        before = s[0:i*j]
        isFirst = True
        Samecnt = 1
        beforeSamecnt = 1
        result = i
        while i*(j+1) <= length:
            now = s[i*j:i*(j+1)]
            if before==now and isFirst:     #처음 겹치는경우
                result += 1
                isFirst = False
                Samecnt += 1
            elif before!=now:
                result += i
                isFirst = True
                Samecnt = 1
                beforeSamecnt = 1
            else:
                Samecnt += 1

            if len(str(beforeSamecnt)) != len(str(Samecnt)):
                beforeSamecnt *= 10
                result += 1

            j += 1
            before = now
        if i*j < length:
            result += length-i*j

        if min_value > result:
            min_value = result


    return min_value


result= solution(s)
print(result)
