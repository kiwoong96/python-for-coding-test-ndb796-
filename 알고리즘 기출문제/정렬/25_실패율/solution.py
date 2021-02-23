N = 4
stages = [4,4,4,4,4]

def solution(N,stages):
    stage = [0 for _ in range(N+2)]
    for data in stages:
        stage[data] += 1
    result = []

    length = len(stages)


    for i in range(1,N+1):
        if length == 0:
            result.append((i,0))
            continue
        result.append((i,stage[i]/length))
        length -= stage[i]

    result.sort(key= lambda x:(-x[1],x[0]))
    answer = []
    for k in result:
        answer.append(k[0])
    return answer

result = solution(N,stages)

print(result)

