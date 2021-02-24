import sys
input = sys.stdin.readline

A = input().strip('\n')
B = input().strip('\n')

def solution(A,B):
    len_A = len(A)
    len_B = len(B)

    dp = [[0 for _ in range(len_A+1)] for _ in range(len_B+1)]

    for i in range(1,len_B+1):
        dp[i][0] = i
    for j in range(1,len_A+1):
        dp[0][j] = j
    #dp[1][1] = 0


    for i in range(1,len_B+1):
        for j in range(1,len_A+1):
            if A[j-1] == B[i-1]:
                #비교하는 두 문자가 같은 경우 왼쪽위 값
                dp[i][j] = dp[i-1][j-1]
            else:
                #비교하는 두 문자가 다른 경우
                #1. 윗 값 + 1 (삭제)
                #2. 왼쪽 값 + 1 (추가)
                #3. 왼쪽 윗 값 + 1 (수정)
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
    for k in dp:
        print(k)
    return dp[len_B][len_A]

result = solution(A,B)
print(result)