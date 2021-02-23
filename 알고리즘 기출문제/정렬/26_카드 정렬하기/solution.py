import heapq
import sys
input = sys.stdin.readline

N = int(input())
data = []

for i in range(N):
    heapq.heappush(data,int(input()))




def solution(data):
    answer = 0
    while len(data)>=2:
        A = heapq.heappop(data)
        B = heapq.heappop(data)
        C = A+B
        answer += C
        heapq.heappush(data,C)

    return answer

answer = solution(data)
print(answer)


