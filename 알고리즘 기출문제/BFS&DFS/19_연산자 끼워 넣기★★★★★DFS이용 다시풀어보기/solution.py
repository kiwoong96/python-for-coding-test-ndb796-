from itertools import permutations
import sys
input = sys.stdin.readline
INF = int(1e9)
N = int(input())
#피연산
operand = list(map(int,input().split()))
#연산자
operator = list(map(int,input().split()))

poss_operator = []
for i in range(len(operator)):
    if operator[i] !=0:
        for j in range(operator[i]):
            poss_operator.append(i)


def solution(operand,operator):
    operator_combination = set(permutations(poss_operator, N-1))
    max_val = -INF
    min_val = INF

    for operator in operator_combination:
        result = operand[0]
        for i in range(len(operator)):
            if operator[i] == 0:
                result += operand[i+1]
            elif operator[i] == 1:
                result -= operand[i+1]
            elif operator[i] == 2:
                result *= operand[i+1]
            else:
                if result <0:
                    result *= -1
                    result //= operand[i+1]
                    result *= -1
                else:
                    result //= operand[i+1]
        if min_val<= result <=max_val:
            continue
        if result < min_val:
            min_val = result
        if result > max_val:
            max_val = result
    return min_val, max_val

min_val, max_val = solution(operand,operator)


print(max_val)
print(min_val)