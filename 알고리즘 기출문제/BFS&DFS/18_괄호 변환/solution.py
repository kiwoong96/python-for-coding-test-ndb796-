from collections import deque
import sys
sys.setrecursionlimit(10**7)
inpt1 = "(()())()"
inpt2 = ")("
inpt3 = "()))((()"

def function(s,rst):
    result = [0,0]
    idx = 0
    for i in range(len(s)):
        if s[i] == "(":
            result[0] +=1
        else:
            result[1] +=1
        if result[0] == result[1]:
            idx = i
            break
    u = s[:idx+1]
    v = s[idx+1:]
    print("u : ", u ,", v :" , v)
    #u가 올바른 문자열인지 확인
    queue = deque()
    is_correct = True
    for i in u:
        if i=='(':
            queue.append(i)
        else:
            if queue:
                queue.popleft()
            else:
                is_correct = False
                break


    #u가 올바른 문자열인 경우
    if is_correct:
        rst += u

        if v:
            print(rst, "is_correct : ", is_correct)
            rst = function(v,rst)

    else:
        rst += '('
        print(rst, "is_correct : ", is_correct)
        rst = function(v,rst)
        rst += ')'
        for i in u[1:-1]:
            if i == '(':
                rst +=')'
            else:
                rst += '('
    return rst








def solution(p):
    answer = ''
    answer = function(p,answer)
    return answer

result = solution(inpt3)
print(result)
