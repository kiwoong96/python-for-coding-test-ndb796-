import sys
input = sys.stdin.readline

S = input().strip('\n')

Ssumation = []
sumation = 0
for data in S:
    if ord(data)-65 < 0:
        sumation += int(data)
    else:
        Ssumation.append(data)

Ssumation.sort()
result = ''

##print(''.join(Ssumation))
for data in Ssumation:
    result +=data
result += str(sumation)
print(result)
