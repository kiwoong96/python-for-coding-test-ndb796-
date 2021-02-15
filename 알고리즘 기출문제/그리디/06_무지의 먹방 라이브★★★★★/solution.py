import heapq

def solution(food_items, k):
    if sum(food_items) <= k:
        return -1

    q = []

    for i in range(len(food_items)):
        heapq.heappush(q,(food_items[i],i+1))

    before = 0
    sum_value = 0
    length = len(q)

    while sum_value + (q[0][0] - before) * length < k:
        now = heapq.heappop(q)[0]
        sum_value += (now - before) * length
        length -= 1
        before = now

    q.sort(key = lambda x:x[1])
    result = q[(k-sum_value)%length][1]
    return result

food_items = [3,1,2]
k = 5
result = solution(food_items,k)

print(result)

